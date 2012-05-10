from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50, help_text="Suggest value...must be unique.")
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/categories/%s/" %self.slug

class Firm(models.Model):
    #Basic Information
    address_1 = models.CharField(max_length=75)
    address_2 = models.CharField(max_length=75)
    categories = models.ManyToManyField(Category)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    firm_name = models.CharField(max_length=75)
    overview = models.TextField(max_length=255)
    owner = models.ForeignKey(User)
    phone = models.IntegerField(max_length=15)
    state = models.CharField(max_length=50)
    website = models.URLField(max_length=200)
    zip_code = models.IntegerField(max_length=5)

    # class Meta:
        # ordering = ['Type']
    
    def __unicode__(self):
        return self.firm_name
    
    def save(self, force_insert=False, force_update=False):
        self.firm_overview_html
          
    def get_absolute_url(self):
        return "/firms/%s/" %self.firm_name
    
    

        