from django import forms
from .models import Region, Province, CityMunicipality

class RegionForm(forms.Form):
    region = forms.ModelChoiceField(
        queryset=Region.objects.order_by("region_name"),
        empty_label="-- Select a region --",
    )

class ProvinceForm(forms.Form):
    province = forms.ModelChoiceField(
        queryset=Province.objects.none(),
        empty_label="-- Select a province --",
    )

class CityMunicipalityForm(forms.Form):
    city_municipality =forms.ModelChoiceField(
        queryset=CityMunicipality.objects.none(),
        empty_label="-- Select a city/municipality --",
    )