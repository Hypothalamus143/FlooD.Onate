from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUser
from ..profiles.models import Profile
from ..accounts.models import CivilianAccount
# Create your views here.
def register(request):
    if(request.method == "POST"):
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            CivilianAccount.objects.create(user=user)
            messages.success(request, "Registered Successfully")
            return redirect("login:login")
    else:
       if request.user.is_authenticated:
           return redirect("home:home")
       form = RegisterUser()
    return render(request, "register/register.html", {"form" : form})
