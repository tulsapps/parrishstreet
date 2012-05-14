from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from apps.firms.models import Firm, Sector 

firm_info_dict = {
                  'queryset': Firm.objects.all()
                  }

urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "firms/firms.html"}, name="firms" ), 
    url(r"^sectors$", direct_to_template, 
        {"template": "firms/sector_list.html"}, 
        'django.views.generic.list_detail.object_list',
        {'queryset': Sector.objects.all()}),                      
)