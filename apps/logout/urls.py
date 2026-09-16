from . import views
from django.urls import path

app_name='logout'

urlpatterns = [
    path("", views.logout, name="logout")
]