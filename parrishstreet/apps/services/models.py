from django.db import models
from django.contrib.auth.models import User

from tagging.fields import TagField 

from apps.profiles.models import Profile
from apps.firms.models import Firm 

import datetime

class Service(models.Model):
    # Meta Data
    consultant = models.ForeignKey(Profile or Firm)
    service_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    tag = TagField()
    service_description = models.TextField(max_length=500)
    value_equation = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        ordering = ['service_name']
        
    def __unicode__(self):
        return self.service_name
    
    def get_absolute_url(self):
        return "/services/%s/"  %self.service_name
    get_absolute_url = models.permalink(get_absolute_url)