from django.db import models, transaction
from ..accounts.models import OfficialAccount
from ..location.models import Baranggay
# Create your models here.
class DonationDrive(models.Model):
    official_account = models.ForeignKey(OfficialAccount, on_delete=models.CASCADE)
    baranggay = models.ForeignKey(Baranggay, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.DecimalField(decimal_places=2, max_digits=10)
    target_amount = models.DecimalField(decimal_places=2, max_digits=12)
    gathered_amount = models.DecimalField(decimal_places=2, max_digits=12)
    status = models.IntegerField()

class Receipt(models.Model):
    pk = models.CompositePrimaryKey('donation_drive', 'receipt_no')
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    receipt_no = models.PositiveIntegerField(editable=False)
    receipt_image = models.ImageField(upload_to="receipts/")

    def save(self, *args, **kwargs):
        if not self.receipt_no:
            with transaction.atomic():
                receipt_nos = Receipt.objects.filter(donation_drive=self.donation_drive).select_for_update()
                max_receipt_no = receipt_nos.aggregate(models.MAX(max_receipt_no='receipt_no'))['max_receipt_no']
                self.receipt_no = (max_receipt_no or 0) + 1
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
class EventPhoto(models.Model):
    pk = models.CompositePrimaryKey('donation_drive', 'event_photo_no')
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    event_photo_no = models.PositiveIntegerField(editable=False)
    event_photo_image = models.ImageField(upload_to="event_photos/")
    def save(self, *args, **kwargs):
            if not self.event_photo_no:
                with transaction.atomic():
                    event_photo_nos = EventPhoto.objects.filter(donation_drive=self.donation_drive).select_for_update()
                    max_event_photo_no = event_photo_nos.aggregate(models.MAX(max_event_photo_no='event_photo_no'))['max_event_photo_no']
                    self.receipt_no = (max_event_photo_no or 0) + 1
                    super().save(*args, **kwargs)
            else:
                super().save(*args, **kwargs)
class AffidavitOfLiquidation(models.Model):
    pk = models.CompositePrimaryKey('donation_drive', 'affidavit_of_liquidation_no')
    donation_drive = models.ForeignKey(DonationDrive, on_delete=models.CASCADE)
    affidavit_of_liquidation_no = models.PositiveIntegerField(editable=False)
    affidavit_of_liquidation_image = models.ImageField(upload_to="affidavit_of_liquidations/")
    transcript = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    def save(self, *args, **kwargs):
            if not self.affidavit_of_liquidation_no:
                with transaction.atomic():
                    affidavit_of_liquidation_nos = AffidavitOfLiquidation.objects.filter(donation_drive=self.donation_drive).select_for_update()
                    max_affidavit_of_liquidation_no = affidavit_of_liquidation_nos.aggregate(models.MAX(max_affidavit_of_liquidation_no='affidavit_of_liquidation_no'))['max_affidavit_of_liquidation_no']
                    self.receipt_no = (max_affidavit_of_liquidation_no or 0) + 1
                    super().save(*args, **kwargs)
            else:
                super().save(*args, **kwargs)