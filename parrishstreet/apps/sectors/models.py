from django.db import models
from django.db.models import validators


class Sector(models.Model):
    sector_name = models.CharField(help_text='Sectors are from the US Census')
    description = models.TextField(blank=True, help_text='Optional')
    slug = models.SlugField(prepopulate_from=('sector_name',))
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    naics_code = models.IntegerField(help_text='from US Census')
    
    class Admin:
        list_display = ('name', '_parents_repr')
    
    def __str__(self):
        p_list = self._recurse_for_parents(self)
        p_list.append(self.name)
        return self.get_separator().join(p_list)
    
    def get_absolute_url(self):
        if self.parent.id:
            return "/sectors/%s/%s/" %(self.parent.slug, self.slug)
        else:
            return "/sectors/%s/" %(self.slug)
        
    def _recurse_for_parents(self, cat_obj):
        p_list = []
        if cat_obj.parent_id:
            p = cat_obj.parent
            p_list.append(p.name)
            more = self._recurse_for_parents(p)
            p_list.extend(more) 
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list
    
    def get_separator(self):
        return '::'

    def _parents_repr(self):
        p_list = self._recurse_for_parents(self)
        return self.get_separator().join(p_list)
    _parents_repr.short_description = "Tag parents"

    def save(self):
        p_list = self._recurse_for_parents(self)
        if self.name in p_list:
            raise validators.ValiationError("You must not save a category in itself!")
        super(Sector, self).save()
    
    
    
    
    
    
    
    
    
    
    