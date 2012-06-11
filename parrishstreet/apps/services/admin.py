from django.contrib import admin
from apps.services.models import Service

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ['service_name']}

admin.site.register(Service, ServiceAdmin)