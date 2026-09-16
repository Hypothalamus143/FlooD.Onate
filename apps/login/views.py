from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect("home:home")
            
    else:
        if request.user.is_authenticated:
            return redirect("home:home")
        form = AuthenticationForm()
    return render(request, "login/login.html", {"form":form})