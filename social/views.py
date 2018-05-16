from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy

@login_required
def dashboard_view(request):
    return render(request, 'social/dashboard.html', {'section':'dashboard'})

def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print (cd['username'], cd['password'], user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    error = 'User Disabled'
            else:
                error = 'Wrong username/password'
        else:
            error = 'Wrong form'
    else:
        form = LoginForm()
    return render(request, 'social/login.html', {'form':form, 'error':error})

def register_view(request):
    error = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            usr = User.objects.filter(username=cd['username'])
            if usr and len(usr) > 0:
                error = 'User Exists'
            elif cd['password'] != cd['confirmPassword']:
                error = 'Password not match'
            else:
                usr = User.objects.create_user(cd['username'], cd['email'], cd['password'])
                prof = Profile.objects.create(user=usr, age=cd['age'])
                prof.save()
                login(request, usr)
                return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'social/register.html', {'form':form, 'error':error})

def logout_view(request):
    logout(request)
    return redirect('login')