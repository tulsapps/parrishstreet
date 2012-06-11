from django.contrib import admin
from apps.products.models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug': ['product_name']}

admin.site.register(Product, ProductAdmin)