from django.shortcuts import render, redirect
from ..verification_request.models import VerificationRequest
from ..accounts.models import ModeratorAccount
from ..users.models import User
# Create your views here.
def moderator(request):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    verification_requests = VerificationRequest.objects.all()
    return render(request, "moderator/moderator.html", {"verification_requests":verification_requests})
def verification_details(request, id):
    if(not ModeratorAccount.objects.filter(user=request.user).first()):
        return redirect("home:home")
    user = User.objects.get(id=id)
    verification_request = VerificationRequest.objects.get(user=user)
    return render(request, "moderator/verification_details.html", {"verification_request":verification_request})