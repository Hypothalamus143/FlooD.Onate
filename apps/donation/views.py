from django.shortcuts import render, redirect
from .models import Donation
from ..accounts.models import CivilianAccount
from ..donation_drive.models import DonationDrive
from .forms import DonationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def donation(request, donation_drive_id):
    civilian_account = CivilianAccount.objects.get(user=request.user)
    donation_drive = DonationDrive.objects.get(id=donation_drive_id)
    if request.method == "POST":
        form = DonationForm(request.POST, request.FILES)
        donation = form.save(commit=False)
        donation.civilian_account = civilian_account
        donation.donation_drive = donation_drive
        donation.save()
        return redirect("donation_drive:donation_drive_details", donation_drive_id)
    else:
        form = DonationForm()
        return render(request, "donation/donation.html", {"form":form})