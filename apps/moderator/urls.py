from django.urls import path
from . import views

app_name = "moderator"

urlpatterns = [
    path('', views.moderator, name='moderator'),
    path('verification_requests', views.verification_requests, name='verification_requests'),
    path('<int:id>/', views.verification_details, name='verification_details'),
    path('moderators', views.moderators, name='moderators'),
    path('non_moderators', views.non_moderators, name='non_moderators'),
]
