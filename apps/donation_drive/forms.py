from django import forms
from .models import DonationDrive

class DonationDriveForm(forms.ModelForm):
    class Meta:
        model = DonationDrive
        fields = ["baranggay", "start_date", "duration", "target_amount"]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }