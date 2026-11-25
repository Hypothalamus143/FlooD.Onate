from django.shortcuts import render, redirect, get_object_or_404
from ..users.models import User
from .models import VerificationRequest
from .forms import VerificationRequestForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def verification_request(request):
    user = request.user
    verification_request = VerificationRequest.objects.filter(user=user).first()
    if request.method == "POST":
        form = VerificationRequestForm(request.POST, request.FILES, instance=verification_request)
        if form.is_valid():
            verificationrequest = form.save(commit=False)
            verificationrequest.user = user
            verification_request.status = 0
            verificationrequest.save()
            return redirect("verification_request:verification_request")
    else:
        form = VerificationRequestForm(instance=verification_request)
        return render(request, "verification_request/verification_request.html", {"form":form, "verification_request": verification_request})