from django.db import models

from stocks.models import Warehouse
from products.models import Product


class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    telephone = models.CharField(max_length=15)
    warehouse = models.ForeignKey(Warehouse)

    def __str__(self):
        return self.name


class Salesperson(models.Model):
    store = models.ForeignKey(Store)
    register_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RetailSales(models.Model):
    store = models.ForeignKey(Store)
    salesperson = models.ForeignKey(Salesperson)
    serial_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    closed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'retail sales'

    def __str__(self):
        if self.serial_number:
            return "{} - {}".format(self.serial_number, self.store)
        else:
            return "Unclosed - {}".format(self.store)

    def clean(self):
        if self.serial_number == "":
            self.serial_number = None

    def total_price(self):
        total = 0
        for line in self.retailsalesline_set.all():
            total += line.total_price()
        return total


class RetailSalesLine(models.Model):
    retail_sales = models.ForeignKey(RetailSales)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return "{} in {}".format(self.product, self.retail_sales)

    def total_price(self):
        return self.quantity * self.unit_price
