from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from stocks.models import *


class Price(models.Model):
    stock = models.OneToOneField(Stock, related_name='wholesales_price')
    cost = models.DecimalField(max_digits=12, decimal_places=4)
    base = models.DecimalField(max_digits=12, decimal_places=4)
    lowest = models.DecimalField(max_digits=12, decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.stock)


class Partner(models.Model):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wholesales-partner-detail', args=[self.pk])


class Location(models.Model):
    partner = models.ForeignKey(Partner)
    name = models.CharField(max_length=5)
    address = models.TextField()

    def __unicode__(self):
        return '{} - {}'.format(self.partner, self.address)


class Purchase(models.Model):
    partner = models.ForeignKey(Partner)

    def __unicode__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse('wholesales-purchase-detail', args=[self.pk])

    def total_price(self):
        total = 0
        for line in self.purchaseline_set.all():
            total += line.price()
        return total


class Line(models.Model):
    stock = models.ForeignKey(Stock)
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    quantity = models.IntegerField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return '{} line'.format(self.purchase, self.stock)

    def price(self):
        return self.unit_price * self.quantity


class PurchaseLine(Line):
    purchase = models.ForeignKey(Purchase)

    def __unicode__(self):
        return '{} - {}'.format(self.purchase, self.stock)


class PurchaseOrder(models.Model):
    purchase = models.OneToOneField(Purchase)

    def __unicode__(self):
        return self.pk


class PurchaseInvoice(models.Model):
    purchase = models.OneToOneField(Purchase)
    number = models.IntegerField()

    def __unicode__(self):
        return self.pk


class Term(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Sale(models.Model):
    partner = models.ForeignKey(Partner)
    served_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse('wholesales-sale-detail', args=[self.pk])

    def total_price(self):
        total = 0
        for line in self.saleline_set.all():
            total += line.price()
        return total


class SaleLine(Line):
    sale = models.ForeignKey(Sale)

    def __unicode__(self):
        return '{} - {}'.format(self.sale, self.stock)


class SaleOrder(models.Model):
    sale = models.OneToOneField(Sale)
    date = models.DateField(auto_now_add=True)
    term = models.ForeignKey(Term)
    closed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.pk
