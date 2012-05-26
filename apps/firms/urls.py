from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail

from apps.firms.models import Firm, Sector

firm_list_info = {
                   'queryset' : Firm.objects.all(),
                   'template_name': 'firms/firm_index.html',
                   'allow_empty': True,
                   #'template_object_name': 'firm_list',
}

sector_list_info = {
                     'queryset': Sector.objects.all(),
                     'template_name': 'firms/sector_index.html',
                     'allow_empty': True,                   
}

urlpatterns = patterns("",
    url(r"^$", list_detail.object_list, firm_list_info, name='firms'),
    url(r"^(?P<object_id>\d+)/$", list_detail.object_detail, firm_list_info, name='firm_detail'),
    url(r"^sectors$", list_detail.object_list, sector_list_info, name='sectors'),                 
)