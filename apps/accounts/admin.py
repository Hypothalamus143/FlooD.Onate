from django.contrib import admin


from .models import ModeratorAccount, OfficialAccount
# Register your models here.
admin.site.register(ModeratorAccount)
admin.site.register(OfficialAccount)