from django.shortcuts import render, redirect, get_object_or_404
from ..users.models import User
from ..user_settings.models import UserSettings
# Create your views here.
def user_settings(request):
    if request.method == "POST":
        dark_mode = request.POST.get("dark_mode")
        email_notifications = request.POST.get("email_notifications")
        username = request.session.get("username")
        user = get_object_or_404(User, username=username)
        user_settings = get_object_or_404(UserSettings, user=user)
        print(email_notifications)
        user_settings.email_notifications = email_notifications == "on"
        user_settings.dark_mode = dark_mode == "on"
        user_settings.save()
        return redirect("user_settings:user_settings")
    if request.session.get('username', False):
        username = request.session.get('username', False)
        user = User.objects.get(username=username)
        user_settings = UserSettings.objects.get(user=user)
        return render(request, "user_settings/user_settings.html", {"user_settings":user_settings})
    else:
        return redirect("login:login")
    