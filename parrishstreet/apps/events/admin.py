from django.contrib import admin
from apps.events.models import Event

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ['event_name']}

admin.site.register(Event, EventAdmin)