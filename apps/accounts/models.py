from django.db import models
from ..users.models import User

# Create your models here.
class CivilianAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()
class ModeratorAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.__str__()
class OfficialAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    def __str__(self):
        return self.user.__str__()
    