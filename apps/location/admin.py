from django.contrib import admin


from .models import Baranggay, Region, Province, CityMunicipality
# Register your models here.
admin.site.register(Baranggay)
admin.site.register(Region)
admin.site.register(Province)
admin.site.register(CityMunicipality)
