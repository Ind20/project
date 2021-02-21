from django.shortcuts import render
from django.http import HttpResponse
from .models import project, projectCategory

def projects(request):
    projects = project.objects.all()
    return render(request,'project/projects.html', {'projects': projects})

def category(request, id):
    cat = projectCategory.objects.get(id=id)
    context = {
             'cat':cat,
            }
    return render(request, 'project/category.html', context)

def categories(request):
    categories = projectCategory.objects.all()
    return render(request,'project/categories.html', {'categories': categories})

def project_detail(request, id):
    proj = project.objects.get(id=id)
    context = {
             'proj':proj,
            }
    return render(request, 'project/project.html', context)