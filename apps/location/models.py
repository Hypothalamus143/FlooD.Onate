from django.db import models
# Create your models here.
class Region(models.Model):
    region_name = models.CharField(max_length=50)

class Province(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    province_name = models.CharField(max_length=50)


class CityMunicipality(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city_municipality_name = models.CharField(max_length=50)

class Baranggay(models.Model):
    city_municipality = models.ForeignKey(CityMunicipality, on_delete=models.CASCADE)
    baranggay_name = models.CharField(max_length=50)