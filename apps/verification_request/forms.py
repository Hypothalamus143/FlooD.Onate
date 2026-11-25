from django import forms
from .models import VerificationRequest

class VerificationRequestForm(forms.ModelForm):
    class Meta:
        model = VerificationRequest
        fields = ["front_id", "back_id", "selfie", "incumbency_cert"]

class VerificationRequestManagementForm(forms.ModelForm):
    class Meta:
        model = VerificationRequest
        fields = ["status", "message"]