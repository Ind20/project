from django.conf.urls import url
from django.urls import path, re_path
from . import views

urlpatterns =[
    url(r'^$', views.projects, name='products'),
    url(r'^/[a-z,0-9]$', views.project_detail, name='project_detail')
]