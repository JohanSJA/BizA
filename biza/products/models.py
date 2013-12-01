from django.db import models


class Unit(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    barcode = models.CharField(max_length=30, unique=True)
    unit = models.ForeignKey(Unit)

    def __unicode__(self):
        return self.name

class Component(models.Model):
    product = models.ForeignKey(Product)
    component = models.ForeignKey(Product, related_name='product_set')
    quantity = models.SmallIntegerField()

    def __unicode__(self):
        return '{} {} in {}'.format(self.quantity, self.component, self.product)
