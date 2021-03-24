from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns =[
    path('', views.home, name='djlogin/home'),
    path('accounts/login/', views.please_login, name='please_login'),

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),
    path('contactus', views.contactus, name='contactus'),

    path('projects', views.projects, name='projects'),
    path('project/<int:id>', views.project_detail, name='project_detail'),
    path('user/<int:id>/projects', views.user_projects, name='user_projects'),
    path('user/<int:u_id>/project/<int:id>', views.user_project, name='user_project'),
    path('addproject', views.addproject, name='addproject'),
    path('editproject/<int:id>', views.editproject, name="editproject"),

    path('categories', views.categories, name='categories'),
    path('category/<int:id>', views.category, name='category'),
    path('category/<int:cat_id>/project/<int:id>', views.category_project, name='category_project'),
    path('category/<int:id>/projects', views.category_projects, name='category_projects'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/announce', views.announce, name='announce'),
    path('dashboard/projects', views.dprojects, name='dprojects'),
    path('dashboard/project/<int:id>', views.dproject, name='dproject'),
    path('announcements', views.announcements, name='announcements'),
    path('announcement/<int:id>', views.announcement_detail, name='announcement_detail'),
    
    path('publish/<int:id>', views.publish, name='publish'),
    path('unpublish/<int:id>', views.unpublish, name='unpublish')
]