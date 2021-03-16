from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import userProfile, projectCategory, project
from .forms import projectForm, contactusMessageForm, userProfileForm, userUpdateForm, userProfileUpdateForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import user_passes_test



def home(request):
    categories = projectCategory.objects.all().order_by('id')[:4]
    projects = project.objects.all().order_by('-id')[:4]
    return render(request, 'main/home.html', {'categories': categories, 'projects': projects})


def header(request):
    return render(request, 'main/header.html')


def footer(request):
    return render(request, 'main/footer.html')


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    return render(request, 'user/dashboard.html')


def contactus(request):
    form = contactusMessageForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Form submitted successfully')
        return redirect('contactus')
    else:
        return render(request, 'main/contactus.html', {'form': form})


def please_login(request):
    msg = "You need to be logged-in to view this page"
    messages.info(request, msg)
    return render(request, 'user/login.html')


def login(request):
    if request.user.is_authenticated:
        messages.info(request,'You are alredy logged in.')
        return redirect('/')
    else:
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
    if request.user.is_authenticated:
        messages.info(request,'You are alredy registered.')
        return redirect('/')
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
                messages.info(request,'Account created successfully.')
                return redirect('login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
    else:
        return render(request,"user/register.html")



@login_required
def profile (request):
    p_form = userProfileForm(instance=request.user.userprofile)
    return render(request, 'user/profile.html', {'p_form': p_form})


@login_required
def editprofile(request):
    if request.method =='POST':
        u_form = userUpdateForm(request.POST or None, instance=request.user)
        p_form = userProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.info(request,'Your profile successfully saved.')
        return redirect('profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = userProfileUpdateForm(instance=request.user.userprofile)
        return render(request, 'user/editprofile.html', {'u_form': u_form, 'p_form': p_form})


def logout(request):
    auth.logout(request)
    messages.info(request,'You are successfully logged out.')
    return redirect('login')


def projects(request):
    if 'key' in request.GET:
        key = request.GET['key']
        projects= project.objects.filter(Project_Name__icontains=key)
        n = len(projects)
        msg = "Showing "'%s' % n + " results for "'"%s"' % key
        if n < 1:
            msg = "No results found for "'"%s"' % key 
            messages.info(request, msg)
        else:
            messages.info(request, msg)
    else:
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


def category_projects(request, id):
    category = projectCategory.objects.get(id=id)
    if 'key' in request.GET:
        key = request.GET['key']
        projects= project.objects.filter(Project_Name__icontains=key, Project_Category_id=id)
        n = len(projects)
        msg = "Showing "'%s' % n + " results for "'"%s"' % key
        if n < 1:
            msg = "No results found for "'"%s"' % key +" in this category"
            messages.info(request, msg)
        else:
            messages.info(request, msg)
    else:
        projects = project.objects.filter(Project_Category_id=id)
    return render(request, 'project/category-projects.html', {'category':category, 'projects': projects})


def category_project(request, cat_id, id):
    proj = project.objects.get(id=id)
    return render(request, 'project/project.html', {'proj': proj})

@login_required
def addproject(request):
    form= projectForm(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Project submitted successfully')
        return redirect('/addproject')
    else:
        return render(request, 'project/addproject.html', {'form': form})