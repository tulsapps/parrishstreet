from django.contrib import admin
from firms.models import Category, Firm

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title'] }

admin.site.register(Category, CategoryAdmin)

class FirmAdmin(admin.ModelAdmin):
    pass

admin.site.register(Firm, FirmAdmin)