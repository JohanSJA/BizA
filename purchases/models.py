from django.db import models

from partners.models import Partner
from products.models import Product


class Supplier(models.Model):
    code = models.CharField(max_length=10, unique=True)
    partner = models.OneToOneField(Partner)

    def __str__(self):
        return str(self.partner)


class PurchaseOrder(models.Model):
    serial_number = models.CharField(max_length=20)
    supplier = models.ForeignKey(Supplier)
    issuing_date = models.DateField()

    class Meta:
        unique_together = ["serial_number", "supplier"]

    def __str__(self):
        return "{} - {}".format(self.supplier, self.serial_number)

    def total_price(self):
        total = 0
        for line in self.purchaseorderline_set.all():
            total += line.total_price()
        return total


class PurchaseOrderLine(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return "{} in {}".format(self.product, self.purchase_order)

    def total_price(self):
        return self.quantity * self.unit_price


class Invoice(models.Model):
    serial_number = models.CharField(max_length=20)
    supplier = models.ForeignKey(Supplier)
    issuing_date = models.DateField()
    payment_due_date = models.DateField()
    payment_made_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ["serial_number", "supplier"]

    def __str__(self):
        return "{} - {}".format(self.serial_number, self.supplier)

    def total_price(self):
        total = 0
        for line in self.invoiceline_set.all():
            total += line.total_price()
        return total


class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4)

    def __str__(self):
        return "{} in {}".format(self.product, self.purchase)

    def total_price(self):
        return self.quantity * self.price


class DeliveryOrder(models.Model):
    serial_number = models.CharField(max_length=20)
    supplier = models.ForeignKey(Supplier)
    issuing_date = models.DateField()
    good_received_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ["serial_number", "supplier"]

    def __str__(self):
        return "{} - {}".format(self.serial_number, self.supplier)

    def total_quantity(self):
        total = 0
        for line in self.deliveryorderline_set.all():
            total += line.quantity
        return total


class DeliveryOrderLine(models.Model):
    delivery_order = models.ForeignKey(DeliveryOrder)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return "{} in {}".format(self.product, self.delivery_order)
