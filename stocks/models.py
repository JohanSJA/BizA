from django.db import models
from django.core.urlresolvers import reverse


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Stock(models.Model):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    unit = models.ForeignKey(Unit)
    discontinued = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stocks-stock-detail', kwargs={'pk': self.pk})


class Warehouse(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()

    def __unicode__(self):
        return self.name


class Balance(models.Model):
    REASONS = [
        ('P', 'Purchase'),
        ('S', 'Sales'),
        ('T', 'Transfer'),
    ]

    stock = models.ForeignKey(Stock)
    warehouse = models.ForeignKey(Warehouse)
    changes = models.IntegerField()
    reason = models.CharField(max_length=1, choices=REASONS)
    amount = models.IntegerField()

    def __unicode__(self):
        return '{} {} in {}'.format(self.amount, self.stock, self.warehouse)
