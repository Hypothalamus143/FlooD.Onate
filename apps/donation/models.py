from django.db import models
from ..accounts.models import CivilianAccount
from ..donation_drive.models import DonationDrive
# Create your models here.

class Donation(models.Model):
    civilian_account = models.ForeignKey(CivilianAccount, on_delete=models.CASCADE)
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    donated_amount = models.DecimalField(max_digits=12, decimal_places=2)
    used_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    returned_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    donation_reference_no = models.CharField(max_length=100)
    donation_reference_image = models.ImageField(
        upload_to="donation_reference_images/"
    )
    return_reference_no = models.CharField(max_length=100, blank=True, null=True)
    return_reference_image = models.ImageField(
        blank=True,
        null = True,
        upload_to="return_reference_images/"
    )
    
    class Status(models.IntegerChoices):
        PENDING = 0, "PENDING"
        ACCEPTED = 1, "ACCEPTED"
        REJECTED = 2, "REJECTED"
    status = models.IntegerField(
        choices=Status.choices,
        default = Status.PENDING
    )
    message = models.TextField(null=True, blank=True)

    def __str__(self):
            return f"{self.civilian_account.__str__()} - {self.id}"