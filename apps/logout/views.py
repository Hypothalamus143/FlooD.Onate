from django.shortcuts import redirect
from django.contrib import auth

# Create your views here.
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("login:login")
    else:
        return redirect("home:home")