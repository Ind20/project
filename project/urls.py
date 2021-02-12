from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    url(r'^$', views.projects, name='products'),
    url(r'^(?P<projectID>[a-z,0-9]+)/$', views.project_detail, name='project_detail')
]