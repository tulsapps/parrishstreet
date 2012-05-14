from django.db import models
from django.contrib.auth.models import User

from markdown import markdown
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
    # Summary Data
    owner = models.ForeignKey(User)
    firm_name = models.CharField(max_length=75)
    firm_overview = models.TextField(editable=False, blank=True)
    value_proposition = models.TextField(editable=False, blank=True)
    tag = TagField()
    featured = models.BooleanField(default=False)
    
    # Physical Location Data
    address_1 = models.CharField(max_length=75)
    address_2 = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    #lng = 
    #lat = 
    
    # Virtual Location Data
    #website = models.URLField(unique=True)
    #email = models.EmailField(max_length=254)
    #phone = models.CharField(max_length=15)

    
    #class Meta:
        #ordering = ['']
    
    def __unicode__(self):
        return self.firm_name
    
    def save(self, force_insert=False, force_update=False):
        self.firm_overview = markdown(self.firm_overview)
        if self.value_proposition:
            self.value_proposition_html = markdown(self.value_proposition)
        super(Firm, self).save(force_insert, force_update)
          
    def get_absolute_url(self):
        return "/firms/%s/" %self.firm_name
    
    

        