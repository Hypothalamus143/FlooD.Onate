from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('official_account', views.official_account, name='official_account'),
    path('civilian_account', views.civilian_account, name='civilian_account'),
]
