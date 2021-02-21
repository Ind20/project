from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns =[
    path('/categories', views.categories, name="categories"),
    path('/category/<int:id>/', views.category, name='category'),
    path('/projects', views.projects, name="projects"),
    path('/project/<int:id>/', views.project_detail, name='project_detail')
    
]