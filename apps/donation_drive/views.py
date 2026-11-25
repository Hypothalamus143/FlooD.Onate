from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..accounts.models import OfficialAccount, CivilianAccount
from .models import DonationDrive, Receipt, EventPhoto, AffidavitOfLiquidation
from .forms import DonationDriveForm, ReceiptForm, EventPhotoForm, AffidavitOfLiquidationForm
from ..donation.models import Donation
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
def donation_drive_management(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    if official_account is None:
        return redirect("home:home")
    donation_drive = DonationDrive.objects.get(id=id, official_account=official_account)
    donations = Donation.objects.filter(donation_drive=donation_drive)
    receipts = Receipt.objects.filter(donation_drive=donation_drive)
    return render(request, "donation_drive/donation_drive_management.html", {"donation_drive":donation_drive, "official_account":official_account, "donations":donations, "receipts":receipts})

@login_required
def create_donation_drive(request):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    if official_account is None:
        return redirect("home:home")
    if request.method == "POST":
        form = DonationDriveForm(request.POST)
        if form.is_valid():
            donation_drive = form.save(commit=False)
            donation_drive.official_account = official_account
            donation_drive.save()
            return redirect("donation_drive:official_account_donation_drives")
    form = DonationDriveForm()
    return render(request, "donation_drive/create_donation_drive.html", {"form":form})

@login_required
def create_receipt(request, donation_drive_id):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    donation_drive = DonationDrive.objects.get(id=donation_drive_id, official_account=official_account)
    if official_account is None:
        return redirect("home:home")
    if request.method == "POST":
        form = ReceiptForm(request.POST, request.FILES
        )
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.donation_drive = donation_drive
            receipt.save()
            print("valid")
            return redirect("donation_drive:donation_drive_management", donation_drive_id)
    form = ReceiptForm()
    return render(request, "donation_drive/create_receipt.html", {"form":form})