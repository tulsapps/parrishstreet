from django.shortcuts import get_object_or_404, render_to_response
from apps.products.models import Product

def product_index(request):
    return render_to_response('products/products_index.html',
                              {'sector_list': Product.objects.all()},
)