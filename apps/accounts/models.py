from django.db import models
from ..users.models import User

# Create your models here.
class CivilianAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class ModeratorAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class OfficialAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    