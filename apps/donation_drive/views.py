from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..accounts.models import OfficialAccount, CivilianAccount
from .models import DonationDrive, Receipt, EventPhoto, AffidavitOfLiquidation
from .forms import DonationDriveForm, ReceiptForm, EventPhotoForm, AffidavitOfLiquidationForm
from ..location.forms import RegionForm, ProvinceForm, CityMunicipalityForm
from ..location.models import Region, Province, CityMunicipality, Baranggay
from ..donation.models import Donation
from django.db.models import Sum
from django.urls import reverse
from django.utils import timezone
from urllib.parse import urlencode

# Create your views here.
@login_required
def donation_drives(request):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    donation_drives = DonationDrive.objects.all()
    official_account_id = request.GET.get("official_account_id")
    baranggay_id = request.GET.get("baranggay_id")
    if official_account_id:
        donation_drives = donation_drives.filter(official_account_id=official_account_id)
    if baranggay_id:
            donation_drives = donation_drives.filter(baranggay_id=baranggay_id)
    return render(request, "donation_drive/donation_drives.html", {"donation_drives":donation_drives, "official_account":official_account})

@login_required
def donation_drive_details(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    civilian_accont = CivilianAccount.objects.get(user=request.user)
    donation_drive = DonationDrive.objects.get(id=id)
    donations = Donation.objects.filter(donation_drive=donation_drive)
    receipts = Receipt.objects.filter(donation_drive=donation_drive)
    event_photos = EventPhoto.objects.filter(donation_drive=donation_drive)
    affidavit_of_liquidations = AffidavitOfLiquidation.objects.filter(donation_drive=donation_drive)
    gathered_amount = donations.filter(status=1).aggregate(gathered_amount=Sum("donated_amount"))
    used_amount = affidavit_of_liquidations.aggregate(used_amount=Sum("amount"))
    return render(request, "donation_drive/donation_drive_details.html", {"donation_drive":donation_drive, "official_account":official_account, "civilian_account":civilian_accont, "donations":donations, "receipts":receipts, "event_photos": event_photos, "affidavit_of_liquidations":affidavit_of_liquidations, "gathered_amount":gathered_amount, "used_amount":used_amount})

@login_required
def create_donation_drive(request, city_municipality_id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    if official_account is None:
        return redirect("home:home")
    queryset = Baranggay.objects.filter(city_municipality_id=city_municipality_id)
    if request.method == "POST":
        form = DonationDriveForm(request.POST)
        form.fields["baranggay"].queryset = queryset
        if form.is_valid():
            donation_drive = form.save(commit=False)
            donation_drive.official_account = official_account
            donation_drive.save()
            query = urlencode({"official_account_id":official_account.id})
            url = f"{reverse('donation_drive:donation_drives')}?{query}"
            return redirect(url)
    form = DonationDriveForm()
    form.fields["baranggay"].queryset = queryset
    return render(request, "donation_drive/create_donation_drive.html", {"form":form})

@login_required
def create_receipt(request, donation_drive_id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
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
            return redirect("donation_drive:donation_drive_details", donation_drive_id)
    form = ReceiptForm()
    return render(request, "donation_drive/create_receipt.html", {"form":form})

@login_required
def create_event_photo(request, donation_drive_id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
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
            return redirect("donation_drive:donation_drive_details", donation_drive_id)
    form = EventPhotoForm()
    return render(request, "donation_drive/create_event_photo.html", {"form":form})

@login_required
def create_affidavit_of_liquidation(request, donation_drive_id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
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
            return redirect("donation_drive:donation_drive_details", donation_drive_id)
    form = AffidavitOfLiquidationForm()
    return render(request, "donation_drive/create_affidavit_of_liquidation.html", {"form":form})

@login_required
def receipt_details(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    receipt = Receipt.objects.get(id=id)
    if request.method == "POST":
        form = ReceiptForm(request.POST, request.FILES, instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("donation_drive:receipt_details", id)
    if official_account == receipt.donation_drive.official_account:
        form = ReceiptForm(instance=receipt)
    else:
        form = None
    return render(request, "donation_drive/receipt_details.html", {"official_account":official_account, "receipt":receipt, "form":form})

@login_required
def event_photo_details(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    event_photo = EventPhoto.objects.get(id=id)
    if request.method == "POST":
        form = EventPhotoForm(request.POST, request.FILES, instance=event_photo)
        if form.is_valid():
            form.save()
            return redirect("donation_drive:event_photo_details", id)
    if official_account == event_photo.donation_drive.official_account:
        form = EventPhotoForm(instance=event_photo)
    else:
        form = None
    return render(request, "donation_drive/event_photo_details.html", {"official_account":official_account, "event_photo":event_photo, "form":form})

@login_required
def affidavit_of_liquidation_details(request, id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    affidavit_of_liquidation = AffidavitOfLiquidation.objects.get(id=id)
    if request.method == "POST":
        form = AffidavitOfLiquidationForm(request.POST, request.FILES, instance=affidavit_of_liquidation)
        if form.is_valid():
            form.save()
            return redirect("donation_drive:affidavit_of_liquidation_details", id)
    if official_account == affidavit_of_liquidation.donation_drive.official_account:
        form = AffidavitOfLiquidationForm(instance=affidavit_of_liquidation)
    else:
        form = None
    return render(request, "donation_drive/affidavit_of_liquidation_details.html", {"official_account":official_account, "affidavit_of_liquidation":affidavit_of_liquidation, "form":form})

@login_required
def select_region(request):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    if(official_account is None):
        return redirect("home:home")
    if request.method == "POST":
        form =  RegionForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            region = cleaned["region"]
            return redirect("donation_drive:select_province", region.id)
    form = RegionForm()
    return render(request, "donation_drive/create_donation_drive.html", {"official_account":official_account, "form":form})

@login_required
def select_province(request, region_id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    if(official_account is None):
        return redirect("home:home")
    queryset = Province.objects.filter(region_id=region_id)
    if request.method == "POST":
        form =  ProvinceForm(request.POST)
        form.fields["province"].queryset = queryset
        if form.is_valid():
            cleaned = form.cleaned_data
            province = cleaned["province"]
            return redirect("donation_drive:select_city_municipality", province.id)
    form = ProvinceForm()
    form.fields["province"].queryset = queryset
    return render(request, "donation_drive/create_donation_drive.html", {"official_account":official_account, "form":form})

@login_required
def select_city_municipality(request, province_id):
    official_account = OfficialAccount.objects.filter(user=request.user).filter(expiry_date__lt=timezone.localdate()).first()
    if(official_account is None):
        return redirect("home:home")
    queryset = CityMunicipality.objects.filter(province_id=province_id)
    if request.method == "POST":
        form =  CityMunicipalityForm(request.POST)
        form.fields["city_municipality"].queryset = queryset
        if form.is_valid():
            cleaned = form.cleaned_data
            city_municipality = cleaned["city_municipality"]
            return redirect("donation_drive:create_donation_drive", city_municipality.id)
    form = CityMunicipalityForm()
    form.fields["city_municipality"].queryset = queryset
    return render(request, "donation_drive/create_donation_drive.html", {"official_account":official_account, "form":form})
