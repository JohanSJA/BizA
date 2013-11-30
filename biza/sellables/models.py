from django.db import models


class Unit(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50, unique=True)
    allow_fraction = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class TaxConstant(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    tax_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    commission = models.DecimalField(max_digits=20, decimal_places=2)
    tax_constant = models.ForeignKey(TaxConstant)
    parent = models.ForeignKey('self')

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

class Sellable(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    barcode = models.CharField(max_length=30, unique=True)
    cost = models.DecimalField(max_digits=20, decimal_places=4)
    base_price = models.DecimalField(max_digits=20, decimal_places=2)
    notes = models.TextField(blank=True)
    max_discount = models.DecimalField(max_digits=20, decimal_places=2)
    commission = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    unit = models.ForeignKey(Unit)
    category = models.ForeignKey(Category)
    tax_constant = models.ForeignKey(TaxConstant)

    def __unicode__(self):
        return self.name
