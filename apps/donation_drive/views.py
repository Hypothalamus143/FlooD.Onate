from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..accounts.models import OfficialAccount, CivilianAccount
from .models import DonationDrive, Receipt, EventPhoto, AffidavitOfLiquidation
from .forms import DonationDriveForm, ReceiptForm, EventPhotoForm, AffidavitOfLiquidationForm
from ..donation.models import Donation
# Create your views here.
@login_required
def donation_drives(request):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    donation_drives = DonationDrive.objects.all()
    official_account_id = request.GET.get("official_account_id")
    if official_account_id:
        donation_drives = donation_drives.filter(official_account_id=official_account_id)
    return render(request, "donation_drive/donation_drives.html", {"donation_drives":donation_drives, "official_account":official_account})

@login_required
def donation_drive_details(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    civilian_accont = CivilianAccount.objects.get(user=request.user)
    donation_drive = DonationDrive.objects.get(id=id)
    donations = Donation.objects.filter(donation_drive=donation_drive)
    receipts = Receipt.objects.filter(donation_drive=donation_drive)
    event_photos = EventPhoto.objects.filter(donation_drive=donation_drive)
    affidavit_of_liquidation = AffidavitOfLiquidation.objects.filter(donation_drive=donation_drive)
    return render(request, "donation_drive/donation_drive_details.html", {"donation_drive":donation_drive, "official_account":official_account, "civilian_account":civilian_accont, "donations":donations, "receipts":receipts, "event_photos": event_photos, "affidavit_of_liquidation":affidavit_of_liquidation})

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
            return redirect("donation_drive:donation_drive_management", donation_drive_id)
    form = ReceiptForm()
    return render(request, "donation_drive/create_receipt.html", {"form":form})

@login_required
def create_event_photo(request, donation_drive_id):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    donation_drive = DonationDrive.objects.get(id=donation_drive_id, official_account=official_account)
    if official_account is None:
        return redirect("home:home")
    if request.method == "POST":
        form = EventPhotoForm(request.POST, request.FILES
        )
        if form.is_valid():
            event_photo = form.save(commit=False)
            event_photo.donation_drive = donation_drive
            event_photo.save()
            return redirect("donation_drive:donation_drive_management", donation_drive_id)
    form = EventPhotoForm()
    return render(request, "donation_drive/create_event_photo.html", {"form":form})

@login_required
def create_affidavit_of_liquidation(request, donation_drive_id):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    donation_drive = DonationDrive.objects.get(id=donation_drive_id, official_account=official_account)
    if official_account is None:
        return redirect("home:home")
    if request.method == "POST":
        form = AffidavitOfLiquidationForm(request.POST, request.FILES
        )
        if form.is_valid():
            affidavit = form.save(commit=False)
            affidavit.donation_drive = donation_drive
            affidavit.save()
            return redirect("donation_drive:donation_drive_management", donation_drive_id)
    form = AffidavitOfLiquidationForm()
    return render(request, "donation_drive/create_affidavit_of_liquidation.html", {"form":form})

@login_required
def receipt_details(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).first()
    receipt = Receipt.objects.get(id=id)
    if request.method == "POST":
        form = ReceiptForm(request.POST, request.FILES
        )
        if form.is_valid():
            receipt.save()
            return redirect("donation_drive:receipt_details", id)
    if official_account == receipt.donation_drive.official_account:
        form = ReceiptForm(instance=receipt)
    else:
        form = None
    return render(request, "donation_drive/receipt_details.html", {"official_account":official_account, "receipt":receipt, "form":form})