from django.db import models
from django.core.urlresolvers import reverse


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

    def get_absolute_url(self):
        return reverse('products_product_detail', args=[str(self.id)])

class Component(models.Model):
    product = models.ForeignKey(Product)
    component = models.ForeignKey(Product, related_name='product_set')
    quantity = models.SmallIntegerField()

    def __unicode__(self):
        return '{} {} in {}'.format(self.quantity, self.component, self.product)

class Warehouse(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()

    def __unicode__(self):
        return self.name

class Quantity(models.Model):
    product = models.ForeignKey(Product)
    warehouse = models.ForeignKey(Warehouse)
    datetime = models.DateTimeField(auto_now=True)
    changes = models.IntegerField()
    balance = models.IntegerField()

    class Meta:
        verbose_name_plural = 'quantities'

    def __unicode__(self):
        return '{} {} at {}'.format(self.balance, self.product, self.warehouse)
