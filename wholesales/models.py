from django.db import models

from partners.models import Partner
from products.models import Product


class Salesperson(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SalesTerm(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    telephone = models.CharField(max_length=15, blank=True)
    fax = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    salesperson = models.ForeignKey(Salesperson)
    sales_term = models.ForeignKey(SalesTerm)

    def __str__(self):
        return self.name


class SalesOrder(models.Model):
    customer = models.ForeignKey(Customer)
    issuing_date = models.DateField()
    sales_term = models.ForeignKey(SalesTerm)

    def __str__(self):
        return self.id

    def total_price(self):
        total = 0
        for line in self.salesorderline_set.all():
            total += line.total_price()
        return total


class SalesOrderLine(models.Model):
    sales_order = models.ForeignKey(SalesOrder)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return "{} in {}".format(self.product, self.sales_order)

    def total_price(self):
        return self.quantity * self.unit_price


class SalesDeliveryOrder(models.Model):
    customer = models.ForeignKey(Customer)
    address = models.TextField()
    issuing_date = models.DateField()
    good_sent_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.id

    def total_quantity(self):
        total = 0
        for line in self.salesdeliveryorderline_set.all():
            total += line.quantity
        return total


class SalesDeliveryOrderLine(models.Model):
    delivery_order = models.ForeignKey(SalesDeliveryOrder)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return "{} in {}".format(self.product, self.delivery_order)
