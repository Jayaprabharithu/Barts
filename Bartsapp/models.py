from django.db import models

# Create your models here.
class Category_db(models.Model):
    Category_Name=models.CharField(max_length=100,blank=True,null=True)
    Description=models.CharField(max_length=100,blank=True,null=True)
    Category_image=models.ImageField(upload_to="category images",null=True,blank=True)

class sub_categorydb(models.Model):
    Category=models.CharField(max_length=100,blank=True,null=True)
    subcategory_name=models.CharField(max_length=100,blank=True,null=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=100,blank=True,null=True)
    Terms_conditions=models.CharField(max_length=100,blank=True,null=True)
    sub_categoryimage=models.ImageField(upload_to="category images",null=True,blank=True)

class Projectdb(models.Model):
    Client_name=models.CharField(max_length=100,blank=True,null=True)
    Work_year=models.IntegerField(blank=True,null=True)
    Started_date=models.DateField(null=True,blank=True)
    Finished_date=models.DateField(blank=True,null=True)
    Image1=models.ImageField(upload_to="category images",null=True,blank=True)
    Image2=models.ImageField(upload_to="category images",null=True,blank=True)
    Image3=models.ImageField(upload_to="category images",null=True,blank=True)
    Image4=models.ImageField(upload_to="category images",null=True,blank=True)
    Image5=models.ImageField(upload_to="category images",null=True,blank=True)



