from django.db import models
from django.core.urlresolvers import reverse_lazy


class Uom(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'unit of measurement'
        verbose_name_plural = 'units of measurement'

    def __unicode__(self):
        return self.name


class Stock(models.Model):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=50, unique=True)
    note = models.TextField(blank=True)
    uom = models.ForeignKey(Uom, verbose_name='UOM')
    discontinued = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('stocks-stock-detail', kwargs={'pk': self.pk})

    def is_package(self):
        if self.components.all():
            return True
        else:
            return False
    is_package.boolean = True

    def balance(self):
        balance = 0
        for log in self.log_set.all():
            balance = balance + log.balance()
        return balance


class Component(models.Model):
    stock = models.ForeignKey(Stock, related_name='components')
    content = models.ForeignKey(Stock, related_name='packages')
    quantity = models.SmallIntegerField()

    class Meta:
        unique_together = [('stock', 'content')]

    def __unicode__(self):
        return '{} {} {} in {}'.format(self.quantity, self.content.uom, self.content, self.stock)


class Warehouse(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('stocks-warehouse-detail', kwargs={'pk': self.pk})

    def balance(self):
        balance = 0
        for log in self.log_set.all():
            balance = balance + log.balance()
        return balance


class Log(models.Model):
    warehouse = models.ForeignKey(Warehouse)
    stock = models.ForeignKey(Stock)

    class Meta:
        unique_together = [('warehouse', 'stock')]

    def __unicode__(self):
        return '{} in {}'.format(self.stock, self.warehouse)

    def get_absolute_url(self):
        return reverse_lazy('stocks-log-detail', kwargs={'pk': self.pk})

    def balance(self):
        balance = self.entry_set.aggregate(models.Sum('changes'))
        if balance['changes__sum']:
            return balance['changes__sum']
        else:
            return 0


class Entry(models.Model):
    REASONS = [
        ('RS', 'Retails Sales'),
        ('WP', 'Wholesales Purchase'),
        ('WS', 'Wholesales Sales'),
        ('IT', 'Internal Transfer'),
    ]

    log = models.ForeignKey(Log)
    timestamp = models.DateTimeField(auto_now_add=True)
    changes = models.IntegerField()
    reason = models.CharField(max_length=2, choices=REASONS)

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['-timestamp']

    def __unicode__(self):
        return '{} - {}'.format(self.log, self.timestamp)
