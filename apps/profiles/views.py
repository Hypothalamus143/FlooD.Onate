from django.shortcuts import render, redirect, get_object_or_404
from ..users.models import User
from ..profiles.models import Profile
# Create your views here.
def profile(request):
    if request.method == "POST":
            bio = request.POST.get("bio")
            username = request.session.get("username")
            user = get_object_or_404(User, username=username)
            profile = get_object_or_404(Profile, user=user)
            profile.bio = bio
            profile.save()
            return redirect("profile:profile")
    if request.session.get('username', False):
        username = request.session.get('username', False)
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        return render(request, "profile/profile.html", {"profile":profile, "user": user})
    else:
        return redirect("login:login")
    