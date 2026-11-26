from django.urls import path
from . import views

app_name = "donation"

urlpatterns = [
    path('<int:donation_drive_id>/', views.donation, name='donation'),
    path('donation_details/<int:id>', views.donation_details, name='donation_details'),
]
