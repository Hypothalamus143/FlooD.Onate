from django.urls import path
from . import views

app_name = "donation"

urlpatterns = [
    path('<int:donation_drive_id>/', views.donation, name='donation'),
    path('<int:donation_drive_id>/<int:id>', views.donation_management, name='donation_management'),
]
