import geocoder

from django.db import models

# Create your models here.
# API Key
access_token = ''

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    # Automatically called when saving the object in the database
    # Grabs the latitude and longitude of an address using geocoder API
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=access_token)
        g = g.latlng  # Returns a list [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)  # save method in models.Model class which handles the save function for models created
