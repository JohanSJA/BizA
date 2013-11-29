from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    upc = models.CharField(max_length=30, null=True, blank=True)
    sku = models.CharField(max_length=30, null=True, blank=True)
