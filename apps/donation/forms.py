from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["donated_amount", "donation_reference_no", "donation_reference_image"]