from django.urls import path
from . import views

app_name = "donation_drive"

urlpatterns = [
    path('', views.donation_drive, name='donation_drive'),
    path('create_donation_drive', views.create_donation_drive, name='create_donation_drive'),
]
