from django.db import models

from django.contrib.auth.models import User
from django.contrib.gis.db import models

from tagging.fields import TagField 

class Sector(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    class Meta:
        ordering = ['title']
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/sectors/%s/" %self.slug

class Firm(models.Model):
    # Meta Data
    owner = models.ForeignKey(User, editable=False)
    firm_name = models.CharField(max_length=75, unique=True)
    firm_overview = models.TextField(blank=True)
    value_proposition = models.TextField(max_length=255)
    featured = models.BooleanField(default=False)
    
    # Physical Location Data
    address_1 = models.CharField(max_length=75, blank=True)
    address_2 = models.CharField(max_length=75, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)

    # Virtual Location Data
    #website = models.URLField(unique=True, blank=True)
    #email = models.EmailField(max_length=254)
    #phone = models.CharField(max_length=15, blank=True)
   
    #class Meta:
        #ordering = ['']
    
    def __unicode__(self):
        return self.firm_name
          
    def get_absolute_url(self):
        return "/businesses/%s/" %self.firm_name

#class GeoLocate(models.Model):
    
    

        