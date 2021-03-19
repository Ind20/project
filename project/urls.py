from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns =[
    path('', views.home, name='djlogin/home'),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
    path('contactus', views.contactus, name='contactus'),
    path('categories', views.categories, name="categories"),
    path('category/<int:id>', views.category, name='category'),
    path('category/<int:cat_id>/project/<int:id>', views.category_project, name='category_project'),
    path('category/<int:cat_id>/project/<int:id>', views.category_project, name='category_project'),
    path('category/<int:id>/projects', views.category_projects, name='category_projects'),
    path('projects', views.projects, name="projects"),
    path('project/<int:id>', views.project_detail, name='project_detail'),
    path('addproject', views.addproject, name="addproject"),
    path('editproject/<int:id>', views.editproject, name="editproject"),
    path('accounts/login', views.please_login, name='please_login')
]