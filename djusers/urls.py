from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='djlogin/home'),
    path('user/profile', views.profile, name="profile"),
    path('user/editprofile', views.editprofile, name="editprofile"),
    path('user/register', views.register, name='register'),
    path('user/login', views.login, name='login'),
    path('user/dashboard', views.dashboard, name='dashboard'),
    path('user/logout', views.logout, name='logout'),
    path('djlogin/header', views.header, name='header'),
    path('djlogin/footer', views.footer, name='footer'),
    path('djlogin/contactus', views.contactus, name='contactus')
]