from django.contrib import admin
from apps.firms.models import Firm

class FirmAdmin(admin.ModelAdmin):
    pass

admin.site.register(Firm, FirmAdmin)