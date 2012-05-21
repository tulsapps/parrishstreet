from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail

from apps.products.models import Product

product_list_info = {
                     'queryset': Product.objects.all(),
                     'template_name': 'products/product_index.html',
                     'allow_empty': True,                   
}

urlpatterns = patterns("",
    url(r"^$", list_detail.object_list, product_list_info, name='products'),
)