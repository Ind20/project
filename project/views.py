from django.shortcuts import render
from django.http import HttpResponse
from .models import project

def projects(request):
    projects = project.objects.all()
    return render(request,'project/projects.html',
                  {'projects': projects})

def project_detail(request,productID):
    pd = project.objects.raw('SELECT * FROM project_project WHERE id =%s',[productID])
    for x in pd:
        x
    return render(request,'project/project.html',{'project':project})