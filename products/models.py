from django.db import models


class Uom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=5, blank=True)

    class Meta:
        verbose_name = 'unit of measure'
        verbose_name_plural = 'units of measure'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    uom = models.ForeignKey(Uom)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)
