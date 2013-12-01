from django.db import models

from products.models import Product
from employees.models import Employee as eEmployee


class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

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
