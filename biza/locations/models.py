from django.db import models


class Location(models.Model):
    address = models.TextField()

    def __unicode__(self):
        return self.address
