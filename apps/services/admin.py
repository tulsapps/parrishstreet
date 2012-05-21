from django.contrib import admin
from apps.services.models import Service

class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)