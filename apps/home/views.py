from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
import geopandas as gpd
from ..donation_drive.models import DonationDrive
# Create your views here.

@login_required
def home(request):
    with open("data/philsa_flood_web.geojson", "r", encoding="utf-8") as f:
        flood_geojson = f.read()

    drives = list(
        DonationDrive.objects.select_related("baranggay").values(
            "baranggay__baranggay_name",
            "baranggay__city_municipality",
            "baranggay__latitude",
            "baranggay__longitude",
        )
    )
    return render(request, "home/home.html", {
        "flood_geojson": flood_geojson,
        "drives_json": json.dumps(drives, default=float),
    })