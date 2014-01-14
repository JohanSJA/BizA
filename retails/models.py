from django.db import models

from products.models import Product, Warehouse
from employees.models import Employee as eEmployee


class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    warehouse = models.ForeignKey(Warehouse)

    class Meta:
        verbose_name_plural = 'branches'

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    branch = models.ForeignKey(Branch)
    employee = models.OneToOneField(eEmployee)

    def __unicode__(self):
        return '{} {}'.format(self.branch, self.employee)


class Price(models.Model):
    product = models.ForeignKey(Product)
    branch = models.ForeignKey(Branch)
    cost = models.DecimalField(max_digits=20, decimal_places=4)
    base = models.DecimalField(max_digits=20, decimal_places=2)
    lowest = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        unique_together = ('product', 'branch')

    def __unicode__(self):
        return '{} at {}'.format(self.product, self.branch)


class Sale(models.Model):
    branch = models.ForeignKey(Branch)
    handled_by = models.ForeignKey(eEmployee,
            related_name='handled_sale_set')
    opened_by = models.ForeignKey(eEmployee,
            related_name='opened_sale_set')
    opening_time = models.DateTimeField(auto_now=True)
    closed_by = models.ForeignKey(eEmployee, null=True, blank=True,
            related_name='closed_sale_set')
    closing_time = models.DateTimeField(null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=20, decimal_places=2,
            null=True, blank=True)

    def __unicode__(self):
        return 'Handled by {} at {}'.format(self.handled_by, self.branch)


class SaleLine(models.Model):
    sale = models.ForeignKey(Sale)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.SmallIntegerField()

    def __unicode__(self):
        return '{} {} in {} at {}/{}'.format(
                self.quantity, self.product, self.sale,
                self.price, self.product.unit)
