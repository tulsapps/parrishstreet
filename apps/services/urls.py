from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail

from apps.services.models import Service

service_list_info = {
                     'queryset': Service.objects.all(),
                     'template_name': 'services/service_index.html',
                     'allow_empty': True,                   
}

urlpatterns = patterns("",
    url(r"^$", list_detail.object_list, service_list_info, name='services'),
)