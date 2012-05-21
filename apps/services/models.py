from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    consultant = models.ForeignKey(User, editable=False)
    service_name = models.CharField(max_length=100)
    service_description = models.TextField(max_length=500)
    value_equation = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['service_name']
        
    def __unicode__(self):
        return self.service_name
    
    def get_absolute_url(self):
        return "/services/%s/"  %self.service_name