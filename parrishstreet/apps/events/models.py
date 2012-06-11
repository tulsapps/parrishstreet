from django.db import models

from idios.models import ProfileBase

from tagging.fields import TagField 

import datetime

class EventDescription(models.Model):
    # Meta Data
    event_name = models.CharField(max_length=100)
    big_benefit = models.CharField(max_length=144, 
                                   help_text='what does the attendee gain or avoid by attending?')
    slug = models.SlugField(unique=True)
    tag = TagField()
    event_description = models.TextField(max_length=500, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    event_page = models.URLField(blank=True)
    
    
    class Meta:
        ordering = ['event_name']
        
    def __unicode__(self):
        return self.event_name
    
    def get_absolute_url(self):
        return "/events/%s/"  %self.event_name
    get_absolute_url = models.permalink(get_absolute_url)