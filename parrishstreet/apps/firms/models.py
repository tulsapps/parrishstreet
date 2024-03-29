from django.db import models

from apps.profiles.models import Profile

from django.contrib.gis.db import models

from tagging.fields import TagField 

import datetime 

class Firm(models.Model):
    # Meta Data
    owner = models.ForeignKey(Profile)
    firm_name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(unique=True)
    firm_overview = models.TextField(max_length=255, blank=True)
    best_selling = models.TextField(max_length=155, 
                                    help_text = 'Name of your best-selling product or service')
    value_proposition = models.TextField(max_length=255, blank=True)
    featured = models.BooleanField(default=False)
    tag = TagField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    # Physical Location Data
    address_1 = models.CharField(max_length=75, blank=True)
    address_2 = models.CharField(max_length=75, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)

    # Contact  Data
    website = models.URLField(unique=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    
   
    class Meta:
        ordering = ['firm_name']
    
    def __unicode__(self):
        return self.firm_name
          
    def get_absolute_url(self):
        return "/businesses/%s/" % self.slug
    get_absolute_url = models.permalink(get_absolute_url)    

        