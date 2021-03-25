from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns =[
    path('', views.home, name='djlogin/home'),
    path('contactus', views.contactus, name='contactus'),
    path('announcements', views.announcements, name='announcements'),
    path('announcement/<int:id>', views.announcement_detail, name='announcement_detail'),
    path('accounts/login/', views.please_login, name='please_login'),


    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),

    path('createblog', views.createblog, name='createblog'),
    path('editblog/<int:id>', views.editblog, name='editblog'),
    path('user/<int:id>/blogs', views.myblogs, name='myblogs'),
    path('blog/<int:id>', views.blog_detail, name='blog_detail'),
    path('blogs', views.blogs, name='blogs'),

    path('projects', views.projects, name='projects'),
    path('project/<int:id>', views.project_detail, name='project_detail'),
    path('user/<int:id>/projects', views.user_projects, name='user_projects'),
    path('user/<int:u_id>/project/<int:id>', views.user_project, name='user_project'),
    path('addproject', views.createproject, name='createproject'),
    path('editproject/<int:id>', views.editproject, name="editproject"),

    path('categories', views.categories, name='categories'),
    path('category/<int:id>', views.category, name='category'),
    path('category/<int:cat_id>/project/<int:id>', views.category_project, name='category_project'),
    path('category/<int:id>/projects', views.category_projects, name='category_projects'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/announce', views.announce, name='announce'),
    path('dashboard/projects', views.dprojects, name='dprojects'),
    path('dashboard/project/<int:id>', views.dproject, name='dproject'),
    path('dashboard/announcements', views.dannouncements, name='dannouncements'),
    path('dashboard/announcement/<int:id>', views.dannouncement, name='dannouncement'),
    path('dashboard/blogs', views.dblogs, name='dblogs'),
    path('dashboard/blog/<int:id>', views.dblog, name='dblog'),
    path('dashboard/addblog', views.addblog, name='addblog'),
    path('dashboard/addproject', views.addproject, name='addproject'),
    
    path('publish/<int:id>', views.publish, name='publish'),
    path('unpublish/<int:id>', views.unpublish, name='unpublish')
]