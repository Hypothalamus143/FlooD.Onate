from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..accounts.models import OfficialAccount
from .models import DonationDrive
from .forms import DonationDriveForm
# Create your views here.
@login_required
def donation_drive(request):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    donation_drives = DonationDrive.objects.filter(official_account=official_account)
    if official_account is None:
        return redirect("home:home")
    return render(request, "donation_drive/donation_drive.html", {"donation_drives":donation_drives})

@login_required
def create_donation_drive(request):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    if official_account is None:
        return redirect("home:home")
    if request.method == "POST":
        form = DonationDriveForm(request.POST)
        print("POST")
        if form.is_valid():
            donation_drive = form.save(commit=False)
            donation_drive.official_account = official_account
            donation_drive.save()
            return redirect("donation_drive:donation_drive")
        else:
            print("invalid")
    form = DonationDriveForm()
    return render(request, "donation_drive/create_donation_drive.html", {"form":form})