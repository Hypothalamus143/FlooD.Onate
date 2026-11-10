from django.urls import path
from . import views

app_name = "verification_request"

urlpatterns = [
    path('', views.verification_request, name='verification_request'),
]
