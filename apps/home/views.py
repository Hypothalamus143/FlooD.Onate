from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.

@login_required
def home(request):
    return render(request, "home/home.html")
