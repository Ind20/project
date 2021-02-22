from django.shortcuts import render
from django.http import HttpResponse
from .models import project, projectCategory
from .forms import projectForm

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


def addproject(request):
    form= projectForm(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Project submitted successfully')
        return redirect('/project/addproject')
    else:
        context= {'form': form1 }
    return render(request, 'project/addproject.html')