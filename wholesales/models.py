from django.db import models

from partners.models import Partner
from products.models import Product


class Customer(models.Model):
    code = models.CharField(max_length=10, unique=True)
    partner = models.OneToOneField(Partner)

    def __str__(self):
        return str(self.partner)


class SalesOrder(models.Model):
    serial_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer)
    issuing_date = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.customer, self.serial_number)

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


class SalesInvoice(models.Model):
    serial_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer)
    issuing_date = models.DateField()
    payment_due_date = models.DateField()
    payment_received_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.serial_number, self.customer)

    def total_price(self):
        total = 0
        for line in self.salesinvoiceline_set.all():
            total += line.total_price()
        return total


class SalesInvoiceLine(models.Model):
    invoice = models.ForeignKey(SalesInvoice)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return "{} in {}".format(self.product, self.purchase)

    def total_price(self):
        return self.quantity * self.price


class SalesDeliveryOrder(models.Model):
    serial_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer)
    issuing_date = models.DateField()
    good_sent_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.serial_number, self.customer)

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
