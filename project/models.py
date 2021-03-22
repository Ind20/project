from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField


class userProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num       = models.CharField(max_length = 15)
    age             = models.IntegerField(null=True)
    profile_pic     = models.ImageField(default='assets/profile.png', upload_to='images/profile/', null='true', blank='true')
    @property
    def get_profile_pic(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
         return "images/assets/profile.png"



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
    Project_Category        = models.ForeignKey(projectCategory, on_delete=models.CASCADE)
    Project_Name            = models.CharField(max_length=350)
    Student_Name            = models.CharField(max_length=35)
    Mentor_Name             = models.CharField(max_length=35)
    Project_Video_url       = models.CharField(max_length=2085)
    Project_Description     = RichTextField(null='true', blank='true')
    Project_Image           = models.ImageField(default='assets/project.png', upload_to='images/project/images', null='true', blank='true')
    Attachment              = models.FileField(upload_to='images/project/attachments', null='true', blank='true')
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Project_Name


class announcement(models.Model):
    title           = models.CharField(max_length=350)
    description     = models.CharField( max_length=10000)
    attachment      = models.FileField(upload_to='images/announcement/attachments', null='true', blank='true')
    date_created    = models.DateTimeField(default=datetime.now)           
    
    def __str__(self):
        return self.title
