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
    unit = models.ForeignKey(Unit, verbose_name='UOM')
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
        ('RS', 'Retails Sales'),
        ('WP', 'Wholesales Purchase'),
        ('WS', 'Wholesales Sales'),
        ('IT', 'Internal Transfer'),
    ]

    stock = models.ForeignKey(Stock)
    warehouse = models.ForeignKey(Warehouse)
    changes = models.IntegerField()
    reason = models.CharField(max_length=2, choices=REASONS)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['-timestamp']

    def __unicode__(self):
        return '{} {} in {}'.format(self.amount, self.stock, self.warehouse)
