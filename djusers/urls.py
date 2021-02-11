from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
    path('contactus', views.contactus, name='contactus')
]