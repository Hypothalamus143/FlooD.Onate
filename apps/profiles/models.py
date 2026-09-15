from django.db import models
from ..users.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(
        blank=True,
        null=True,
        upload_to="profiles/"
    )
    def __str__(self):
        return self.user.__str__