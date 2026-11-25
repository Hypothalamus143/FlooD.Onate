from django import forms
from .models import DonationDrive, Receipt, EventPhoto, AffidavitOfLiquidation

class DonationDriveForm(forms.ModelForm):
    class Meta:
        model = DonationDrive
        fields = ["baranggay", "start_date", "duration", "target_amount"]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["receipt_image"]

class EventPhotoForm(forms.ModelForm):
    class Meta:
        model = EventPhoto
        fields = ["event_photo_image"]

class AffidavitOfLiquidationForm(forms.ModelForm):
    class Meta:
        model = AffidavitOfLiquidation
        fields = ["amount", "affidavit_of_liquidation_image", "transcript"]