from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from stocks.models import Warehouse, Product


class Store(models.Model):
    name = models.CharField(max_length=32)
    location = models.TextField()
    telephone = models.CharField(max_length=16)
    email = models.EmailField(blank=True)
    warehouse = models.ForeignKey(Warehouse)

    def __unicode__(self):
        return self.name


class Saleperson(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Sale(models.Model):
    store = models.ForeignKey(Store)
    saleperson = models.ForeignKey(Saleperson)
    opening_time = models.DateTimeField(auto_now_add=True)
    opened_by = models.ForeignKey(User, related_name='opened_sale_set')
    quoting_time = models.DateTimeField(null=True, blank=True)
    quoted_by = models.ForeignKey(User, null=True, blank=True, related_name='quoted_sale_set')
    closing_time = models.DateTimeField(null=True, blank=True)
    closed_by = models.ForeignKey(User, null=True, blank=True, related_name='closed_sale_set')
    cash_bill_number = models.CharField(max_length=12, blank=True)
    quotation_number = models.CharField(max_length=12, blank=True)

    class Meta:
        ordering = ['-opening_time']

    def __unicode__(self):
        return '{:%c} at {}'.format(timezone.localtime(self.opening_time), self.store)

    def get_absolute_url(self):
        return reverse('retails_sale_detail', kwargs={'pk': self.pk})

    def total_amount(self):
        amount = 0
        for line in self.saleline_set.all():
            amount += line.total_amount()
        return amount

    def total_discount(self):
        discount = 0
        for line in self.saleline_set.all():
            discount += line.total_discount()
        return discount

    def total_quantity(self):
        quantity = 0
        for line in self.saleline_set.all():
            quantity += line.quantity
        return quantity

    def get_status(self):
        if self.cash_bill_number:
            return 'Closed'
        elif self.quotation_number:
            return 'Quoted'
        else:
            return 'Open'

    def closed(self):
        if self.cash_bill_number:
            return True
        else:
            return False

    def quoted(self):
        if self.quotation_number:
            return True
        else:
            return False


class SaleLine(models.Model):
    sale = models.ForeignKey(Sale)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=4)
    discount = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)

    class Meta:
        unique_together = ['sale', 'product']

    def __unicode__(self):
        return '{} {} in {}'.format(self.quantity, self.product, self.sale)

    def get_absolute_url(self):
        return reverse('retails_saleline_detail', kwargs={'pk': self.pk})

    def price_after_discount(self):
        if self.discount:
            return self.unit_price - self.discount
        else:
            return self.unit_price

    def total_amount(self):
        return self.quantity * self.price_after_discount()

    def total_discount(self):
        if self.discount:
            return self.quantity * self.discount
        else:
            return 0

    def get_quantity(self):
        if self.product.is_package():
            return '{} SET'.format(self.quantity)
        else:
            return '{} {}'.format(self.quantity, self.product.item.unit_of_measure)
