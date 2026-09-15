from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterUser
from ..profiles.models import Profile
from ..user_settings.models import UserSettings
# Create your views here.
def register(request):
    if(request.method == "POST"):
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            UserSettings.objects.create(user=user)
            messages.success(request, "Registered Successfully")
            return redirect("login:login")
    else:
            form = RegisterUser()
    return render(request, "register/register.html", {"form" : form})
