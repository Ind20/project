from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import userProfile
from .forms import contactusMessageForm, userProfileForm

def home(request):
    return render(request, 'home.html')


def header(request):
    return render(request, 'header.html')


def footer(request):
    return render(request, 'footer.html')

def contactus(request):
    form= contactusMessageForm(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'contactus.html', context)

        
def profile (request):
    profiledatas = userProfile.objects.filter(user = request.user)
    return render(request, 'profile.html', {'data': profiledatas})


def editprofile(request):
    form = userProfileForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)
    if form.is_valid():
        userProfile = form.save(commit=False)
        userProfile.user = request.user
        userProfile.save()
        return redirect('/profile')
    else:
        context = {'form':form }
        return render(request, 'editprofile.html', context)

    


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username/password")
            return redirect('login')
    else:
        return render(request,"login.html")


def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_num = request.POST['phone_num']
        age = request.POST['age']
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
                                      email=email, first_name=first_name,
                                      last_name=last_name)
                user.save()
                newuserProfile = userProfile(phone_num=phone_num, age=age, user=user)
                newuserProfile.save()
                messages.info(request,'Account created.')
                return redirect('login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    messages.info(request,'You are successfully logged out.')
    return redirect('/login')
