from django.db import models

from locations.models import Location


class Warehouse(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name
