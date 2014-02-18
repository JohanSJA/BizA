from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from stocks.models import *


class Price(models.Model):
    stock = models.OneToOneField(Stock, related_name='wholesales_price')
    cost = models.DecimalField(max_digits=12, decimal_places=4)
    base = models.DecimalField(max_digits=12, decimal_places=4)
    lowest = models.DecimalField(max_digits=12, decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.stock)


class Partner(models.Model):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wholesales-partner-detail', args=[self.pk])


class Location(models.Model):
    partner = models.ForeignKey(Partner)
    name = models.CharField(max_length=5)
    address = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.partner, self.address)


class Purchase(models.Model):
    partner = models.ForeignKey(Partner)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('wholesales-purchase-detail', args=[self.pk])

    def total_price(self):
        total = 0
        for line in self.purchaseline_set.all():
            total += line.price()
        return total

    def ordered(self):
        try:
            self.purchaseorder
            return True
        except ObjectDoesNotExist:
            return False
    ordered.boolean = True

    def invoiced(self):
        try:
            self.purchaseinvoice
            return True
        except ObjectDoesNotExist:
            return False
    invoiced.boolean = True



class PurchaseLine(models.Model):
    purchase = models.ForeignKey(Purchase)
    stock = models.ForeignKey(Stock)
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    quantity = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.purchase, self.stock)

    def price(self):
        return self.unit_price * self.quantity


class PurchaseOrder(models.Model):
    purchase = models.OneToOneField(Purchase)

    def __str__(self):
        return str(self.pk)


class PurchaseInvoice(models.Model):
    purchase = models.OneToOneField(Purchase)
    number = models.CharField(max_length=12)

    def __str__(self):
        return self.number


class Term(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    partner = models.ForeignKey(Partner)
    served_by = models.ForeignKey(User)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('wholesales-sale-detail', args=[self.pk])

    def total_price(self):
        total = 0
        for line in self.saleline_set.all():
            total += line.price()
        return total

    def ordered(self):
        try:
            self.saleorder
            return True
        except ObjectDoesNotExist:
            return False
    ordered.boolean = True

    def delivered(self):
        try:
            self.saledelivery
            return True
        except ObjectDoesNotExist:
            return False
    delivered.boolean = True


class SaleLine(models.Model):
    sale = models.ForeignKey(Sale)
    stock = models.ForeignKey(Stock)
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    quantity = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.sale, self.stock)

    def price(self):
        return self.unit_price * self.quantity



class SaleOrder(models.Model):
    sale = models.OneToOneField(Sale)
    date = models.DateField(auto_now_add=True)
    term = models.ForeignKey(Term)

    def __str__(self):
        return str(self.sale)


class SaleDelivery(models.Model):
    sale = models.OneToOneField(Sale)
    date = models.DateField(auto_now_add=True)
    warehouse = models.ForeignKey(Warehouse)
    address = models.ForeignKey(Location)

    def __str__(self):
        return str(self.sale)
