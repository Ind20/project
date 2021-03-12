from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import project, projectCategory
from .forms import projectForm

def projects(request):
    projects = project.objects.all()
    return render(request,'project/projects.html', {'projects': projects})

def project_detail(request, id):
    proj = project.objects.get(id=id)
    return render(request, 'project/project.html', {'proj': proj})

def categories(request):
    categories = projectCategory.objects.all()
    return render(request,'project/categories.html', {'categories': categories})

def category(request, id):
    projects = project.objects.filter(Project_Category_id=id)[:8]
    category = projectCategory.objects.get(id=id)
    return render(request, 'project/category.html', {'category':category, 'projects': projects})

def addproject(request):
    form= projectForm(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Project submitted successfully')
        return redirect('/project/addproject')
    else:
        context= {'form': form }
    return render(request, 'project/addproject.html', context)