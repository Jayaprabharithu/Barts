from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages



from Bartsapp.models import sub_categorydb, Category_db,Projectdb
from bartsweb.forms import RegisterForm, LoginForm
from bartsweb.models import contactdb

# Create your views here.


def home(request):
    cat = Category_db.objects.all()
    scat = sub_categorydb.objects.all()
    Pdata= Projectdb.objects.all()


    return render(request,"home_page.html", {"cat": cat, "scat": scat,"Pdata":Pdata})

def about(request):
    cat = Category_db.objects.all()
    return render(request,"about_page.html",{"cat" : cat})

def contact(request):
    cat = Category_db.objects.all()
    return render(request,"contact_page.html",{"cat" : cat})

def save_contact(req):
    if req.method=="POST":
      a =req.POST.get("name")
      b=req.POST.get("email")
      c=req.POST.get("subject")
      d=req.POST.get("message")
      e=req.POST.get("phone")
      obj=contactdb(Name=a,Email=b,Subject=c,Message=d,Mobile=e)
      obj.save()
      return redirect(contact)


def filltered(request, Cat_Name):
    search = request.POST.get("search")
    if search is None:
        fdata=sub_categorydb.objects.filter(Category=Cat_Name)
    else:
        fdata = sub_categorydb.objects.filter(Category=Cat_Name,subcategory_name__istartswith=search)
    scat = Category_db.objects.all()
    cat=Cat_Name
    return render(request, "filltered.html",{"fdata": fdata, "scat": scat,"cat":cat} )


def single(request,sid):
    scat = sub_categorydb.objects.get(id=sid)
    cat = Category_db.objects.all()
    return render(request, 'single.html',{'scat':scat,'cat':cat} )

def project_details(request):

    Pdata= Projectdb.objects.all()
    cat = Category_db.objects.all()
    return render(request, "Projects.html",{'Pdata':Pdata,'cat':cat} )

def single_project(request,pid):
    pro = Projectdb.objects.get(id=pid)
    cat = Category_db.objects.all()
    return render(request, 'Single_Project.html',{'pro':pro,'cat':cat} )


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page or another appropriate page after successful registration
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            usr = authenticate(request, username=uname, password=pwd)
            if usr:
                login(request, user=usr)
                messages.success(request, 'login successfully')
                return redirect('home')
        messages.error(request, 'invalid credential')
        return render(request, 'login.html', {"form": form})

@login_required(login_url='login')
def log_out_view(request, *args, **kwargs):
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect('home')

