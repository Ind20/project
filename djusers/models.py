from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num       = models.CharField(max_length = 15)
    age             = models.IntegerField(null=True)
    profile_pic     = models.ImageField(default='profile.png', upload_to='images/', null='true', blank='true')
    

class contactusMessage(models.Model):
    fullname        = models.CharField(max_length=35)
    phone_num       = models.CharField(max_length=15)
    email           = models.EmailField()
    message         = models.TextField(max_length=1000)
