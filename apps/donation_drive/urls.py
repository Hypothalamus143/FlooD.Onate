from django.urls import path
from . import views

app_name = "donation_drive"

urlpatterns = [
    path('', views.donation_drive, name='donation_drive'),
]
