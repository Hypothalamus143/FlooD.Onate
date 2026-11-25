from django.db import models, transaction
from ..accounts.models import OfficialAccount
from ..location.models import Baranggay
# Create your models here.
class DonationDrive(models.Model):
    class Status(models.IntegerChoices):
        CLOSED = 0, "CLOSED"
        OPEN = 1, "OPEN"
    official_account = models.ForeignKey(OfficialAccount, on_delete=models.CASCADE)
    baranggay = models.ForeignKey(Baranggay, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.DecimalField(decimal_places=2, max_digits=10)
    target_amount = models.DecimalField(decimal_places=2, max_digits=12)
    gathered_amount = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    status = models.IntegerField(default=Status.OPEN, choices=Status.choices)

    def __str__(self):
        return f"{self.baranggay.__str__()} - {self.official_account.__str__()}"
class Receipt(models.Model):
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    receipt_image = models.ImageField(upload_to="receipts/")

class EventPhoto(models.Model):
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    event_photo_image = models.ImageField(upload_to="event_photos/")

class AffidavitOfLiquidation(models.Model):
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    affidavit_of_liquidation_image = models.ImageField(upload_to="affidavit_of_liquidations/")
    transcript = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)