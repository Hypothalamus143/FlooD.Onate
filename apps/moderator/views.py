from django.shortcuts import render
from ..verification_request.models import VerificationRequest
# Create your views here.
def moderator(request):
    verification_requests = VerificationRequest.objects.all()
    return render(request, "moderator/moderator.html", {"verification_requests":verification_requests})