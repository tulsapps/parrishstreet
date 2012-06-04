from django.conf.urls.defaults import *

from django.views.generic import list_detail

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
                    'allow_empty':True,  
                    'slug_field':'slug',               
}

urlpatterns = patterns("",
    url(r"^$", list_detail.object_list, firm_list_info, name='firms'),
    url(r"^(?P<slug>[-\w]+)/$", list_detail.object_detail, firm_detail_info),                
)