from django.db import models
# Create your models here.
class Region(models.Model):
    region_name = models.CharField(max_length=50)

    def __str__(self):
        return self.region_name
class Province(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    province_name = models.CharField(max_length=50)

    def __str__(self):
        return self.province_name
class CityMunicipality(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city_municipality_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_municipality_name
class Baranggay(models.Model):
    city_municipality = models.ForeignKey(CityMunicipality, on_delete=models.CASCADE)
    baranggay_name = models.CharField(max_length=50)
    latitude = models.DecimalField(decimal_places=8, max_digits=12)
    longitude = models.DecimalField(decimal_places=8, max_digits=12)
    def __str__(self):
        return self.baranggay_name