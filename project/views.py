from django.shortcuts import render
from django.http import HttpResponse
from .models import project

def projects(request):
    projects = project.objects.all()
    return render(request,'project/projects.html', {'projects': projects})

def project_detail(request, id):
    proj = project.objects.get(id=id)
    context = {
             'proj':proj,
            }
    return render(request, 'project/project.html', context)