from django.contrib import admin
from apps.firms.models import Sector, Firm

class SectorAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

admin.site.register(Sector, SectorAdmin)

class FirmAdmin(admin.ModelAdmin):
    pass

admin.site.register(Firm, FirmAdmin)