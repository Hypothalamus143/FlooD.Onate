from django.db import models
from ..users.models import User
# Create your models here.
class VerificationRequest(models.Model):
    class Status(models.IntegerChoices):
        PENDING = 0, "PENDING"
        FOR_REVISION = 1, "FOR_REVISION"
        REJECTED = 2, "REJECTED"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_update_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(
        choices=Status.choices,
        default=Status.PENDING
    )
    message = models.TextField(null=True, blank=True)
    front_id = models.ImageField(upload_to='front_ids/')
    back_id = models.ImageField(upload_to='back_ids/')
    selfie = models.ImageField(upload_to='selfies/')
    incumbency_cert = models.ImageField(upload_to='incumbency_certs/')

