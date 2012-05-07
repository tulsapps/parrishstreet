from django.db import models
from profiles import Profile

    
class Industry(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters. ')
    #slug = models.SlugField(unique=True, help_text='Suggested value automatically generated from title')
    description = models.TextField()
    
    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Industries"
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
       # return "/industries/%s/" %self.slug

class Firm(models.Model):
    LIVE_STATUS = 1
    HIDDEN_STATUS = 2
    STATUS_CHOICES = (
                      (LIVE_STATUS, 'Live'),
                      (HIDDEN_STATUS, 'Hidden'),
                      ) 
    owner = models.ForeignKey(Profile)
    firm_name = models.CharField(max_length=250)
    featured = models.BooleanField(default=False)
    #sponsored = models.BooleanField(default=False)
    value_proposition = models.CharField(max_length=255, help_text='In the simplest way possible explain why people should by from you')
    firm_overview = models.TextField()
    #slug = models.SlugField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    industries = models.ManyToManyField(Industry)
    value_proposition_html = models.TextField(editable=False, blank=True)
    firm_overview_html = models.TextField(editable=False, blank=True)
    
    class Meta:
        ordering = ['Industry']
    
    def __unicode__(self):
        return self.firm_name
    
    #def save(self, force_insert=False, force_update=False):
    #    self.firm_overview_html
    
    #def get_absolute_url:
    #    return
    
    

        