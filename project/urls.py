from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

urlpatterns =[
    url(r'^$', views.projects, name='products'),
     path('/<int:id>', views.project_detail, name='project_detail')
]