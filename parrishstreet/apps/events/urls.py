from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail

from apps.events.models import Event

event_list_info = {
                     'queryset': Event.objects.all(),
                     'template_name': 'events/event_list.html',                  
}

event_detail_info = {
                     'queryset': Event.objects.all(),
                     'template_name': 'events/event_detail.html',
                     'slug_field': 'slug',
                   
}

urlpatterns = patterns("list_detail",
    url(r"^$", list_detail.object_list, event_list_info, name='events'),
    url(r"^(?P<slug>[-\w]+)/$", list_detail.object_detail, event_detail_info, name='event_detail'),
)