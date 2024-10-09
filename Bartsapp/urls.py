from django.urls import path
from Bartsapp import views
urlpatterns=[

        path('index_page/',views.index_page,name="index_page"),
        path('Add_category/',views.Add_category,name="Add_category"),
        path('save_category/',views.save_category,name="save_category"),
        path('Display_category/',views.Display_category,name="Display_category"),
        path('Edit_category/<int:cid>/',views.Edit_category,name="Edit_category"),
        path('Update_category/<int:cid>/',views.Update_category,name="Update_category"),
        path('Delete_category/<int:cid>/',views.Delete_category,name="Delete_category"),

        path('Admin_login/',views.Admin_login,name="Admin_login"),
        path('Login_page/',views.Login_page,name="Login_page"),
        path('Admin_logout/',views.Admin_logout,name="Admin_logout"),


        path('projects/',views.projects,name="projects"),
        path('Add_subcategory/',views.Add_subcategory,name="Add_subcategory"),
        path('save_subcategory/',views.save_subcategory,name="save_subcategory"),
        path('Dispaly_subcategory/',views.Dispaly_subcategory,name="Dispaly_subcategory"),
        path('Edit_subcategory/<int:pid>/', views.Edit_subcategory, name="Edit_subcategory"),
        path('update_subcategory/<int:pid>/', views.update_subcategory, name="update_subcategory"),
        path('delete_subcategory/<int:pid>/', views.delete_subcategory, name="delete_subcategory"),

        path('save_project/', views.save_project, name="save_project"),
        path('Display_project/', views.Display_project, name="Display_project"),
        path('Edit_projects/<int:pid>/', views.Edit_projects, name="Edit_projects"),
        path('Update_Project/<int:pid>/', views.Update_Project, name="Update_Project"),
        path('delete_Project/<int:pid>/', views.delete_Project, name="delete_Project"),




        path('contact_details/',views.contact_details,name="contact_details"),

]