from django.shortcuts import render,redirect
from Bartsapp.models import Category_db,sub_categorydb,Projectdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from bartsweb.models import contactdb
import datetime
# Create your views here.
def index_page(request):
    return render(request,"index.html")

def Add_category(request):
    return render(request,"Add_category.html")

def save_category(req):
    if req.method=="POST":
        a=req.POST.get("cat")
        b=req.FILES['image']
        c = req.POST.get("dis")
        obj=Category_db(Category_Name=a,Category_image=b,Description=c)
        obj.save()
        return redirect(Add_category)

def Display_category(req):
    data=Category_db.objects.all()
    return render(req,"display_category.html",{"data":data})

def Edit_category(req,cid):
    data=Category_db.objects.get(id=cid)
    return render(req,"edit_category.html",{"data":data})

def Update_category(req,cid):
    if req.method=="POST":
        a=req.POST.get("name")
        b=req.POST.get("dis")
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Category_db.objects.get(id=cid).Category_image
        Category_db.objects.filter(id=cid).update(Category_Name=a,Description=b,Category_image=file)
        return redirect(Display_category)

def Delete_category(req,cid):
    Category_db.objects.filter(id=cid).delete()
    messages.error(req,"Delete successfully")
    return redirect(Display_category)

def Admin_login(req):
    return render(req,"Admin_login.html")
def Login_page(request):
    if request.method=="POST":
        un=request.POST.get('Name')
        pwd=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd

                return redirect(index_page)
            else:
                messages.warning(request,"Invalid User name or Password")
                return redirect(Admin_login)
        else:
            messages.warning(request,"User Not Found")
            return redirect(Admin_login)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request,"Log Out")
    return redirect(Admin_login)


def Add_subcategory(req):
    cat = Category_db.objects.all()
    return render(req,"Add_subcategory.html",{'cat':cat})

def save_subcategory(req):
    if req.method=="POST":
        a=req.POST.get("cat_name")
        b=req.POST.get("name")
        c=req.POST.get("price")
        d=req.POST.get("dis")
        f=req.POST.get("terms")
        e=req.FILES['image']
        obj=sub_categorydb(Category=a,subcategory_name=b,Price=c,Description=d,Terms_conditions=f,sub_categoryimage=e)
        obj.save()
        messages.success(req, "Successfully Saved")
        return redirect(Add_subcategory)

def Dispaly_subcategory(req):
    data=sub_categorydb.objects.all()
    return render(req,"Display_subcategory.html",{'data':data})

def Edit_subcategory(req,pid):
    data=sub_categorydb.objects.get(id=pid)
    cat=Category_db.objects.all()
    return render(req,"Edit_subcategory.html",{'data':data,'cat':cat})

def update_subcategory(req,pid):
    if req.method=="POST":
        a=req.POST.get("cat_name")
        b = req.POST.get("name")
        c = req.POST.get("price")
        d = req.POST.get("dis")
        f = req.POST.get("terms")
        try:
            img=req.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=sub_categorydb.objects.get(id=pid).sub_categoryimage
        sub_categorydb.objects.filter(id=pid).update(Category=a,subcategory_name=b,Price=c,Description=d,Terms_conditions=f,sub_categoryimage=file)
        return redirect(Dispaly_subcategory)

def delete_subcategory(req,pid):
    sub_categorydb.objects.filter(id=pid).delete()
    messages.error(req,"Successfully Deleted")
    return redirect(Dispaly_subcategory)

def projects(req):
    return render(req,"Add_Projects.html")
def save_project(req):
    if req.method=="POST":
        a=req.POST.get("name")
        ab=req.POST.get("year")
        b = req.POST.get("syear")
        c = req.POST.get("fyear")
        d = req.FILES['image1']
        e = req.FILES['image2']
        f = req.FILES['image3']
        g = req.FILES['image4']
        h = req.FILES['image5']
        obj=Projectdb(Client_name=a,Work_year=ab,Started_date=b,Finished_date=c,Image1=d,Image2=e,Image3=f,Image4=g,Image5=h)
        obj.save()
        return redirect(projects)

def Display_project(req):
    data=Projectdb.objects.all()
    return render(req,"display_project.html",{"data":data})

def Edit_projects(req,pid):
    data=Projectdb.objects.get(id=pid)
    return render(req,"Edit_Project.html",{'data':data,})
def Update_Project(req,pid):
    if req.method=="POST":
        a=req.POST.get("name")
        b = req.POST.get("work")
        c = req.POST.get("syear")
        d = req.POST.get("fyear")
        try:
            img=req.FILES['image1']
            fs=FileSystemStorage()
            file1=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file1=Projectdb.objects.get(id=pid).Image1
        try:
            img=req.FILES['image2']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Projectdb.objects.get(id=pid).Image2

        try:
            img = req.FILES['image3']
            fs = FileSystemStorage()
            file3 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file3 = Projectdb.objects.get(id=pid).Image3

        try:
            img = req.FILES['image4']
            fs = FileSystemStorage()
            file4 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file4 = Projectdb.objects.get(id=pid).Image4

        try:
            img = req.FILES['image5']
            fs = FileSystemStorage()
            file5 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file5 = Projectdb.objects.get(id=pid).Image5
        Projectdb.objects.filter(id=pid).update(Client_name=a,Work_year=b,Started_date=c,Finished_date=d,Image1=file1,Image2=file,Image3=file3,Image4=file4,Image5=file5)
        return redirect(Display_project)

def delete_Project(req,pid):
    Projectdb.objects.filter(id=pid).delete()
    messages.error(req,"Successfully Deleted")
    return redirect(Display_project)





def contact_details(req):
    data=contactdb.objects.all()
    return render(req,"Contact.html",{'data':data})