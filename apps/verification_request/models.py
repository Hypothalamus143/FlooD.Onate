from django.db import models
from ..users.models import User
# Create your models here.
class VerificationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_update_date = models.DateField()
    status = models.IntegerField()
    message = models.TextField(null=True, blank=True)
    front_id = models.ImageField(upload_to='front_ids/')
    back_id = models.ImageField(upload_to='back_ids/')
    selfie = models.ImageField(upload_to='selfies/')
    incumbency_cert = models.ImageField(upload_to='incumbency_certs/')

