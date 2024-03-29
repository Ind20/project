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
    path('dashboard/projects', views.dprojects, name='dprojects'),
    path('dashboard/project/<int:id>', views.dproject, name='dproject'),
    path('dashboard/announcements', views.dannouncements, name='dannouncements'),
    path('dashboard/announcement/<int:id>', views.dannouncement, name='dannouncement'),
    path('dashboard/editannouncement/<int:id>', views.editannouncement, name='editannouncement'),
    path('dashboard/categories', views.dcategories, name='dcategories'),
    path('dashboard/category/<int:id>', views.dcategory, name='dcategory'),
    path('dashboard/addcategory', views.addcategory, name='addcategory'),
    path('dashboard/editcategory/<int:id>', views.editcategory, name='editcategory'),
    path('dashboard/addproject', views.addproject, name='addproject'),
    path('dashboard/announce', views.announce, name='announce'),
    path('dashboard/editproject/<int:id>', views.deditproject, name='deditproject'),
    
    path('publishp/<int:id>', views.publishp, name='publishp'),
    path('unpublishp/<int:id>', views.unpublishp, name='unpublishp'),
    path('deletep/<int:id>', views.deletep, name='detelep'),
    path('publisha/<int:id>', views.publisha, name='publisha'),
    path('unpublisha/<int:id>', views.unpublisha, name='unpublisha'),
    path('deletea/<int:id>', views.deletea, name='detelea'),
    path('publishc/<int:id>', views.publishc, name='publishc'),
    path('unpublishc/<int:id>', views.unpublishc, name='unpublishc'),
    path('deletec/<int:id>', views.deletec, name='detelec')
]
