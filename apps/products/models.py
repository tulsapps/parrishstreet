from django.db import models 

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    bigbenefit = models.TextField(max_length=500)
    
    class Meta:
        ordering = ['product_name']
    
    def __unicode__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return "/products/%s/" %self.product_name
