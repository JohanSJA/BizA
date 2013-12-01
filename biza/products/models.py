from django.db import models


class Unit(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    barcode = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category)
    unit = models.ForeignKey(Unit)

    def __unicode__(self):
        return self.name

class Component(models.Model):
    product = models.ForeignKey(Product)
    component = models.ForeignKey(Product, related_name='product_set')
    quantity = models.SmallIntegerField()

    def __unicode__(self):
        return '{} {} in {}'.format(self.quantity, self.component, self.product)

class Price(models.Model):
    cost = models.DecimalField(max_digits=20, decimal_places=4)
    base = models.DecimalField(max_digits=20, decimal_places=2)
    lowest = models.DecimalField(max_digits=20, decimal_places=2)

class BasePrice(Price):
    product = models.OneToOneField(Product)

    def __unicode__(self):
        return self.product
