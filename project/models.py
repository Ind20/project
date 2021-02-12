from django.db import models

# Create your models here.

class project(models.Model):
    Project_Category        = models.CharField(max_length=25)
    Project_Name            = models.CharField(max_length=350)
    Student_Name            = models.CharField(max_length=35)
    Mentor_Name             = models.CharField(max_length=35)
    Project_Image_url       = models.CharField(max_length=2085)
    Project_Video_url       = models.CharField(max_length=2085)
    Project_Description     = models.CharField( max_length=2000)
