from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num       = models.CharField(max_length = 15)
    age             = models.IntegerField(null=True)
    profile_pic     = models.ImageField(default='assets/profile.png', upload_to='images/profile/', null='true', blank='true')
    

class contactusMessage(models.Model):
    fullname        = models.CharField(max_length=35)
    phone_num       = models.CharField(max_length=15)
    email           = models.EmailField()
    message         = models.TextField(max_length=1000)


class projectCategory(models.Model):
    Category_Name           = models.CharField(max_length=35)
    Category_Description    = models.CharField( max_length=2000)
    Category_Image          = models.ImageField(default='assets/category.png', upload_to='images/category/', null='true', blank='true')

    def __str__(self):
        return self.Category_Name

class project(models.Model):
    Project_Name            = models.CharField(max_length=350)
    Project_Category        = models.ForeignKey(projectCategory, on_delete=models.CASCADE)
    Student_Name            = models.CharField(max_length=35)
    Mentor_Name             = models.CharField(max_length=35)
    Project_Image           = models.ImageField(default='assets/project.png', upload_to='images/project/', null='true', blank='true')
    Project_Video_url       = models.CharField(max_length=2085)
    Project_Description     = models.CharField( max_length=10000)

    def __str__(self):
        return self.Project_Name
