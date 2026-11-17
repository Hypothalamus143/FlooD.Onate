from django.urls import path
from . import views

app_name = "moderator"

urlpatterns = [
    path('', views.moderator, name='moderator'),
    path('<int:id>/', views.verification_details, name='verification_details')
]
