from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from stocks.models import Warehouse, Stock


class Shop(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    warehouse = models.OneToOneField(Warehouse)

    def __str__(self):
        return self.name


class Worker(models.Model):
    shop = models.ForeignKey(Shop)
    worker = models.OneToOneField(User)

    def __str__(self):
        return '{} in {}'.format(self.worker, self.shop)


class Price(models.Model):
    stock = models.OneToOneField(Stock, related_name='retails_price')
    base = models.DecimalField(max_digits=12, decimal_places=4)
    lowest = models.DecimalField(max_digits=12, decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.stock, self.base)


class Sale(models.Model):
    shop = models.ForeignKey(Shop)
    served_by = models.ForeignKey(User, related_name='served_sales')

    def __str__(self):
        return '{} - {}'.format(self.shop, self.pk)

    def get_absolute_url(self):
        return reverse('retails-sale-detail', args=[self.pk])

    def closed(self):
        try:
            self.receipt
            return True
        except ObjectDoesNotExist:
            return False
    closed.boolean = True

    def total_price(self):
        total = 0
        for line in self.line_set.all():
            total += line.price()
        return total


class Line(models.Model):
    sale = models.ForeignKey(Sale)
    stock = models.ForeignKey(Stock)
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    quantity = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.sale, self.stock)

    def price(self):
        return self.quantity * self.unit_price


class Receipt(models.Model):
    sale = models.OneToOneField(Sale)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.sale)
