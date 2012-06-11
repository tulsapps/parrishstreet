from django.conf.urls.defaults import *
from django.conf.urls.defaults import patterns, include, url

from django.views.generic.list_detail import object_list, object_detail

from apps.firms.models import Firm

firm_list_info = {
                   'queryset':Firm.objects.all(),
                   'template_name':'firms/firm_list.html',
                   'allow_empty':True,
                   'template_object_name':'firm',
}

firm_detail_info = {
                    'queryset':Firm.objects.all(),
                    'template_name':'firms/firm_detail.html',  
                    'slug_field':'slug',               
}

urlpatterns = patterns("list_detail",
    url(r"^$", object_list, firm_list_info, name='firms'),
    url(r"^(?P<slug>[-\w]+)/$", object_detail, firm_detail_info),                
)