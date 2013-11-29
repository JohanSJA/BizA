from django.db import models


class Uom(models.Model):
    code = models.CharField(max_length=8, unique=True)
    symbol = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
