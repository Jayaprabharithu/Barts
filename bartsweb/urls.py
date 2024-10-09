from django.urls import path
from bartsweb import views
urlpatterns=[
 path('home/',views.home,name="home"),
 path('about/',views.about,name="about"),
 path('contact/',views.contact,name="contact"),
 path('save_contact/',views.save_contact,name="save_contact"),
 path('filltered/<Cat_Name>/',views.filltered,name="filltered"),
 path('single/<int:sid>/',views.single,name="single"),
 path('project_details/',views.project_details,name="project_details"),
 path('single_project/<int:pid>',views.single_project,name="single_project"),
 path('login/',views.LoginView.as_view(),name='login'),
 path('logout/',views.log_out_view,name='logout'),
 path('register/', views.register, name="register"),

]