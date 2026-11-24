from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..accounts.models import OfficialAccount, CivilianAccount
from .models import DonationDrive
from .forms import DonationDriveForm
# Create your views here.
@login_required

def official_account_donation_drives(request):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    donation_drives = DonationDrive.objects.filter(official_account=official_account)
    if official_account is None:
        return redirect("home:home")
    return render(request, "donation_drive/donation_drives.html", {"donation_drives":donation_drives})

@login_required
def all_donation_drives(request):
    donation_drives = DonationDrive.objects.all()
    return render(request, "donation_drive/donation_drives.html", {"donation_drives":donation_drives})

@login_required
def donation_drive_details(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    civilian_accont = CivilianAccount.objects.get(user=request.user)
    donation_drive = DonationDrive.objects.get(id=id)
    return render(request, "donation_drive/donation_drive_details.html", {"donation_drive":donation_drive, "official_account":official_account, "civilian_account":civilian_accont})

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
            return redirect("donation_drive:official_account_donation_drives")
        else:
            print("invalid")
    form = DonationDriveForm()
    return render(request, "donation_drive/create_donation_drive.html", {"form":form})