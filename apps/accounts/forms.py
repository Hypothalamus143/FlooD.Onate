from django import forms
from .models import OfficialAccount

class OfficialAccountForm(forms.ModelForm):
    class Meta:
        model = OfficialAccount
        fields = ["expiry_date"]
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }