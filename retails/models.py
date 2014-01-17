from django.db import models
from django.contrib.auth.models import User

from stocks.models import Warehouse, Stock


class Shop(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    warehouse = models.OneToOneField(Warehouse)

    def __unicode__(self):
        return self.name


class Worker(models.Model):
    shop = models.ForeignKey(Shop)
    worker = models.OneToOneField(User)

    def __unicode__(self):
        return '{} in {}'.format(self.worker, self.shop)


class Price(models.Model):
    stock = models.OneToOneField(Stock)
    base = models.DecimalField(max_digits=12, decimal_places=4)
    lowest = models.DecimalField(max_digits=12, decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} - {}'.format(self.stock, self.base)


class Sale(models.Model):
    shop = models.ForeignKey(Shop)
    closed_at = models.DateTimeField(null=True, blank=True)
    closed_by = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return '{} - {}'.format(self.shop, self.pk)


class Line(models.Model):
    sale = models.ForeignKey(Sale)
    stock = models.ForeignKey(Stock)
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    quantity = models.IntegerField()

    def __unicode__(self):
        return '{} - {}'.format(self.sale, self.stock)


class Receipt(models.Model):
    sale = models.OneToOneField(Sale)

    def __unicode__(self):
        return '{} - {}'.format(self.pk, self.sale)
