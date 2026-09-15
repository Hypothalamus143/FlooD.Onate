from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.session.get('username', False):
        return render(request, "home/home.html")
    else:
        return redirect("login:login")

def logout(request):
    del request.session['username']
    return redirect("login:login")