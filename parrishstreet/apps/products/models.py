from django.db import models 

from tagging.fields import TagField 

from parrishstreet.apps.profiles.models import Profile
from parrishstreet.apps.firms.models import Firm 

import datetime

class Product(models.Model):
    # Meta Data
    creator = models.ForeignKey(Profile or Firm)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    tag = TagField()
    big_benefit = models.TextField(max_length=500)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    
    class Meta:
        ordering = ['product_name']
    
    def __unicode__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return "/products/%s/" %self.product_name
    get_absolute_url = models.permalink(get_absolute_url)
