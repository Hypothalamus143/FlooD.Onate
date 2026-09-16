from django.shortcuts import render, redirect, get_object_or_404
from ..users.models import User
from .models import UserSettings
from .forms import UserSettingsForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def user_settings(request):
    user = request.user
    instance = UserSettings.objects.get(user=user)
    if request.method == "POST":
        form = UserSettingsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("user_settings:user_settings")
    else:
        form = UserSettingsForm(instance=instance)
        return render(request, "user_settings/user_settings.html", {"form":form})