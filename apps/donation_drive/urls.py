from django.urls import path
from . import views

app_name = "donation_drive"

urlpatterns = [
    path('', views.all_donation_drives, name='all_donation_drives'),
    path('official_account/', views.official_account_donation_drives, name='official_account_donation_drives'),
    path('create_donation_drive', views.create_donation_drive, name='create_donation_drive'),
    path('<int:id>/', views.donation_drive_details, name='donation_drive_details'),
    path('manage/<int:id>/', views.donation_drive_management, name='donation_drive_management'),
    path('create_receipt/<int:donation_drive_id>/', views.create_receipt, name='create_receipt')
]
