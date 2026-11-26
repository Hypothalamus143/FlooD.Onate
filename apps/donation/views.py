from django.shortcuts import render, redirect
from .models import Donation
from ..accounts.models import CivilianAccount, OfficialAccount
from ..donation_drive.models import DonationDrive
from .forms import DonationForm, DonationManagementForm
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

@login_required
def donation_details(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    civilian_account = CivilianAccount.objects.filter(user=request.user).first()
    donation = Donation.objects.get(id=id)
    if(not (civilian_account == donation.civilian_account or official_account == donation.donation_drive.official_account)):
        return redirect("home:home")
    if request.method == "POST":
        form = DonationManagementForm(request.POST, instance=donation)
        form.save()
        return redirect("donation:donation_details", id)
    else:
        form = DonationManagementForm(instance=donation)
        return render(request, "donation/donation_details.html", {"form":form, "donation":donation, "official_account":official_account})