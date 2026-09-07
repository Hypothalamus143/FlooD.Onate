from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterUser
# Create your views here.

def register(request):
    if(request.method == "POST"):
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
            form = RegisterUser()
    return render(request, "users/register.html", {"form" : form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            request.session['username'] = user.username
            request.session['first_name'] = user.first_name
            return redirect("users:home")
            
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form":form})

def home(request):
    if request.session.get('username', False):
        return render(request, "users/home.html")
    else:
        return redirect("users:login")

def logout(request):
    del request.session['username']
    return redirect("users:login")