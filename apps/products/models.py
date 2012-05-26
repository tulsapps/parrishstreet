from django.db import models 

class Product(models.Model):
    # Meta Data
    product_name = models.CharField(max_length=100)
    #big_benefit = models.TextField(max_length=500)
    
    
    class Meta:
        ordering = ['product_name']
    
    def __unicode__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return "/products/%s/" %self.product_name
