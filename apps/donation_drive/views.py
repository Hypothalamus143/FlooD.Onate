from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..accounts.models import OfficialAccount
from .models import DonationDrive
# Create your views here.
@login_required
def donation_drive(request):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    donation_drives = DonationDrive.objects.filter(official_account=official_account)
    if official_account is None:
        return redirect("home:home")
    return render(request, "donation_drive/donation_drive.html", {"donation_drives":donation_drive})