from django.urls import path
from . import views

app_name = "donation_drive"

urlpatterns = [
    path('', views.donation_drives, name='donation_drives'),
    path('create_donation_drive/<int:city_municipality_id>', views.create_donation_drive, name='create_donation_drive'),
    path('<int:id>/', views.donation_drive_details, name='donation_drive_details'),
    path('create_receipt/<int:donation_drive_id>/', views.create_receipt, name='create_receipt'),
    path('create_event_photo/<int:donation_drive_id>/', views.create_event_photo, name='create_event_photo'),
    path('create_affidavit_of_liquidation/<int:donation_drive_id>/', views.create_affidavit_of_liquidation, name='create_affidavit_of_liquidation'),
    path('receipt_details/<int:id>/', views.receipt_details, name='receipt_details'),
    path('event_photo_details/<int:id>/', views.event_photo_details, name='event_photo_details'),
    path('affidavit_of_liquidation_details/<int:id>/', views.affidavit_of_liquidation_details, name='affidavit_of_liquidation_details'),
    path('select_region', views.select_region, name='select_region'),
    path('select_province/<int:region_id>', views.select_province, name='select_province'),
    path('select_city_municipality/<int:province_id>', views.select_city_municipality, name='select_city_municipality'),
]
