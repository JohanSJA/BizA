from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=100, unique=True)
    telephone = models.CharField(max_length=15, blank=True)
    fax = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name
