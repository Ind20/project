from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import userProfile, projectCategory, project, announcement
from .forms import projectForm, contactusMessageForm, userProfileForm, userUpdateForm, userProfileUpdateForm, projectEditForm, announcementForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import user_passes_test



def home(request):
    categories   = projectCategory.objects.all().order_by('id')[:4]
    projects     = project.objects.all().order_by('-id')[:4]
    context = {
    'categories': categories,
    'projects': projects
    }
    return render(request, 'main/home.html', context)


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
        return redirect('profile')
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
        return redirect('profile')
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
    uid = request.user.id
    p_user = proj.user_id
    context = {
        'proj': proj,
        'uid': uid,
        'p_user': p_user
    }
    return render(request, 'project/project.html', context)


def user_projects(request, id):
    projects = project.objects.filter(user_id=id)
    return render(request,'project/userprojects.html', {'projects': projects})


def user_project(request, u_id, id):
    proj = project.objects.get(id=id)
    uid = request.user.id
    p_user = proj.user_id
    context = {
        'proj': proj,
        'uid': uid,
        'p_user': p_user
    }
    return render(request, 'project/project.html', context)


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
    uid = request.user.id
    p_user = proj.user_id
    context = {
        'proj': proj,
        'uid': uid,
        'p_user': p_user
    }
    return render(request, 'project/project.html', context)


@login_required
def addproject(request):
    form= projectForm(request.POST or None, request.FILES or None)
    uid = request.user.id
    if request.method=='POST':
        if form.is_valid():
           project = form.save(commit=False)
           project.user = request.user
           project.save()
        messages.info(request,'Project submitted successfully')
        return redirect('/user/%s/projects' % uid) 
    else:
        return render(request, 'project/addproject.html', {'form': form})


@login_required
def editproject(request, id):
    proj = project.objects.get(id=id)
    form= projectEditForm(request.POST or None, request.FILES or None, instance=proj)
    pid = id
    uid = request.user.id
    p_user = proj.user_id
    if uid != p_user:
        messages.info(request,'You do not have permisson to edit this item')
        return redirect('/user/%s/projects' % uid) 
    else:
        if request.method=='POST':
            if form.is_valid():
                form.save()
            messages.info(request,'Project edited successfully')
            return redirect('/user/%s/project/%s' %(uid, pid))
        else:
            return render(request, 'project/editproject.html', {'form': form, 'proj': proj})


def announcements(request):
    announcements = announcement.objects.all().order_by('-id')[:10]
    return render(request, 'main/announcements.html', {'announcements': announcements})


def announcement_detail(request, id):
    anounce = announcement.objects.get(id=id)
    return render(request, 'main/announcement.html', {'anounce': anounce})


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    projects     = project.objects.all().order_by('-id')[:5]
    context = {
    'projects': projects
    }
    return render(request, 'dashboard/dashboard.html', context)


@user_passes_test(lambda u: u.is_superuser)
def dprojects (request):
    projects     = project.objects.all().order_by('-id')
    context = {
    'projects': projects
    }
    return render(request, 'dashboard/projects.html', context)


@user_passes_test(lambda u: u.is_superuser)
def dproject (request, id):
    proj = project.objects.get(id=id)
    context = {
        'proj': proj
    }
    return render(request, 'dashboard/project.html', context)



@user_passes_test(lambda u: u.is_superuser)
def announce(request):
    form = announcementForm(request.POST or None, request.FILES or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
        messages.info(request,'Announcement submitted successfully')
        return redirect('announcements')
    else:
        return render(request, 'dashboard/announce.html', {'form': form})


    
@user_passes_test(lambda u: u.is_superuser)
def publish(request, id):
    pid = id
    proj = project.objects.get(id=id)
    proj.status = 2
    proj.save()
    return redirect('/dashboard/project/%s' %pid)


@user_passes_test(lambda u: u.is_superuser)
def unpublish(request, id):
    pid = id
    proj = project.objects.get(id=id)
    proj.status = 0
    proj.save()
    return redirect('/dashboard/project/%s' %pid)
