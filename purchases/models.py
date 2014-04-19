from django.db import models

from partners.models import Partner
from products.models import Product


class Supplier(models.Model):
    partner = models.OneToOneField(Partner)

    def __str__(self):
        return str(self.partner)


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier)
    issuing_date = models.DateField()

    def __str__(self):
        return self.id

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


class PurchaseDeliveryOrder(models.Model):
    supplier = models.ForeignKey(Supplier)
    issuing_date = models.DateField()
    good_received_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.id

    def total_quantity(self):
        total = 0
        for line in self.purchasedeliveryorderline_set.all():
            total += line.quantity
        return total


class PurchaseDeliveryOrderLine(models.Model):
    delivery_order = models.ForeignKey(PurchaseDeliveryOrder)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()

    def __str__(self):
        return "{} in {}".format(self.product, self.delivery_order)
