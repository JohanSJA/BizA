from django.db import models


class Uom(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=20, unique=True)
    abbreviation = models.CharField(max_length=5, blank=True)

    class Meta:
        verbose_name = 'unit of measure'
        verbose_name_plural = 'units of measure'

    def __str__(self):
        return self.name

    def get_display_name(self):
        if self.abbreviation:
            return self.abbreviation
        else:
            return self.name


class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    uom = models.ForeignKey(Uom)
    cost = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return self.name
