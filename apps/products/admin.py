from django.contrib import admin
from apps.products.models import Product

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)