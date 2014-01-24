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
    doc_num = models.CharField(max_length=20, verbose_name='Document No.')
    date = models.DateField()
    closed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['partner', 'doc_num']

    def __unicode__(self):
        return '{} - {}'.format(self.partner, self.doc_num)

    def get_absolute_url(self):
        return reverse('wholesales-purchase-detail', args=[self.pk])

    def total_price(self):
        total = 0
        for line in self.purchaseline_set.all():
            total += line.price()
        return total


class PurchaseLine(models.Model):
    purchase = models.ForeignKey(Purchase)
    stock = models.ForeignKey(Stock)
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    quantity = models.IntegerField()

    def __unicode__(self):
        return '{} - {}'.format(self.purchase, self.stock)

    def price(self):
        return self.unit_price * self.quantity


class Term(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Sale(models.Model):
    partner = models.ForeignKey(Partner)
    served_by = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    term = models.ForeignKey(Term)
    doc_num = models.CharField(max_length=20, verbose_name='Document No.', blank=True)
    closed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['partner', 'doc_num']

    def __unicode__(self):
        return '{} - {}'.format(self.partner, self.doc_num)

    def get_absolute_url(self):
        return reverse('wholesales-sale-detail', args=[self.pk])

    def total_price(self):
        total = 0
        for line in self.saleline_set.all():
            total += line.price()
        return total


class SaleLine(models.Model):
    sale = models.ForeignKey(Sale)
    stock = models.ForeignKey(Stock)
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    quantity = models.IntegerField()

    def __unicode__(self):
        return '{} - {}'.format(self.sale, self.stock)

    def price(self):
        return self.unit_price * self.quantity
