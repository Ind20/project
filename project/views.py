from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import userProfile, projectCategory, project
from .forms import projectForm, contactusMessageForm, userProfileForm
from django.views.generic import TemplateView, ListView

def home(request):
    categories = projectCategory.objects.all().order_by('id')[:4]
    projects = project.objects.all().order_by('-id')[:4]
    return render(request, 'main/home.html', {'categories': categories, 'projects': projects})


def header(request):
    return render(request, 'main/header.html')


def footer(request):
    return render(request, 'main/footer.html')


def dashboard(request):
    return render(request, 'user/dashboard.html')


def contactus(request):
    form= contactusMessageForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Form submitted successfully')
        return redirect('contactus')
    else:
        return render(request, 'main/contactus.html', {'form': form})


def profile (request):
    profile = userProfile.objects.filter(user = request.user)
    return render(request, 'user/profile.html', {'profile': profile})


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.info(request,'You are successfully logged in.')
            return redirect('/')
        else:
            messages.info(request,"Invalid username/password")
            return redirect('login')
    else:
        return render(request,"user/login.html")


def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_num = request.POST['phone_num']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is not available')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is alreday registered')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1,
                                      email=email, first_name=first_name, last_name=last_name)
                user.save()
                newuserProfile = userProfile(phone_num=phone_num, user=user)
                newuserProfile.save()
                messages.info(request,'Account created.')
                return redirect('login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
    else:
        return render(request,"user/register.html")


def editprofile(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username is not available')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email is alreday registered')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
            user.save()
    form = userProfileForm(request.POST or None, request.FILES or None, instance=request.user)          
    if form.is_valid():
        userProfile = form.save()
        messages.info(request,'Profile saved successfully')
        return redirect('profile')
    else:
        return render(request, 'user/editprofile.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.info(request,'You are successfully logged out.')
    return redirect('login')


def projects(request):
    if 'key' in request.GET:
        key = request.GET['key']
        placeholder = "Showing results for " + key
        projects= project.objects.filter(Project_Name__icontains=key)
    else:
        projects = project.objects.all()
        placeholder = "Search Projects"
    return render(request,'project/projects.html', {'projects': projects, 'placeholder': placeholder})


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


def category_project(request, cat_id, id):
    proj = project.objects.get(id=id)
    return render(request, 'project/project.html', {'proj': proj})


def addproject(request):
    form= projectForm(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Project submitted successfully')
        return redirect('/addproject')
    else:
        return render(request, 'project/addproject.html', {'form': form})