from django.shortcuts import render
from ..verification_request.models import VerificationRequest
from ..users.models import User
# Create your views here.
def moderator(request):
    verification_requests = VerificationRequest.objects.all()
    return render(request, "moderator/moderator.html", {"verification_requests":verification_requests})
def verification_details(request, id):
    user = User.objects.get(id=id)
    verification_request = VerificationRequest.objects.get(user=user)
    return render(request, "moderator/verification_details.html", {"verification_request":verification_request})