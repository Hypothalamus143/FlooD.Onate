from django.shortcuts import render, redirect, get_object_or_404
from ..users.models import User
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def profile(request):
    user = request.user
    instance = Profile.objects.get(user=user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        form.save()
        return redirect("profile:profile")
    else:
        form = ProfileForm(instance=instance)
        return render(request, "profile/profile.html", {"form":form})