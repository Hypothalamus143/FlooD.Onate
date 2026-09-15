from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUser

# Create your views here.
def register(request):
    if(request.method == "POST"):
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully")
            return redirect("login:login")
    else:
            form = RegisterUser()
    return render(request, "register/register.html", {"form" : form})
