from django.db import models

from django.contrib.gis.db import models

from parrishstreet.apps.profiles.models import Profile
from parrishstreet.apps.firms.models import Firm

class Waypoint(models.Model):
    # Physical Location Data
    address_1 = models.CharField(max_length=75, blank=True)
    address_2 = models.CharField(max_length=75, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip_code = models.CharField(max_length=5, blank=True) 

