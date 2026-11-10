from django.shortcuts import render, redirect, get_object_or_404
from ..users.models import User
from .models import VerificationRequest
from .forms import VerificationRequestForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def verification_request(request):
    user = request.user
    if request.method == "POST":
        form = VerificationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            verificationrequest = form.save(commit=False)
            verificationrequest.user = user
            verificationrequest.save()
            return redirect("verification_request:verification_request")
    else:
        form = VerificationRequestForm()
        return render(request, "verification_request/verification_request.html", {"form":form})