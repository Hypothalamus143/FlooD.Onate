from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True, null=False)
    contact_number = models.CharField(max_length=50, unique=True, null=False)
    birth_date = models.DateField(null=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    REQUIRED_FIELDS = ["email", "contact_number", "birth_date"]