from django.db import models

# Create your models here.

class projectCategory(models.Model):
    Category_Name           = models.CharField(max_length=35)
    Category_Description   = models.CharField( max_length=2000)
    Category_Image          = models.ImageField(default='assets/category.png', upload_to='images/category/', null='true', blank='true')

class project(models.Model):
    Project_Name            = models.CharField(max_length=350)
    Project_Category        = models.ForeignKey(projectCategory, on_delete=models.CASCADE)
    Student_Name            = models.CharField(max_length=35)
    Mentor_Name             = models.CharField(max_length=35)
    Project_Image           = models.ImageField(default='assets/project.png', upload_to='images/project/', null='true', blank='true')
    Project_Video_url       = models.CharField(max_length=2085)
    Project_Description     = models.CharField( max_length=10000)
