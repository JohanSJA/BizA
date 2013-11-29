from django.db import models


class Cashbook(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
