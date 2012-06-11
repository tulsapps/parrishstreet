from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list, object_detail

from apps.sectors.models import Sector



sector_list_info = {
                 'queryset': Sector.objects.all(),
                 'template_name': 'sectors/sector_list.html',
}

sector_detail_info = {
                 'queryset': Sector.objects.all(),
                 'template_name': 'sectors/sector_list.html',
}

urlpatterns = patterns('list_detail',
    url(r'^$/', object_list, sector_list_info, name='sector'),
    url(r'^(?P<slug>[-\w]+)/$', object_detail, sector_detail_info, name='sector_detail'),
                          
)