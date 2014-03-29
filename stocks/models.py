from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import Sum

from products.models import Product


class Uom(models.Model):
    name = models.CharField(max_length=50, unique=True,
            help_text='<em>e.g. meter</em>')
    abbreviation = models.CharField(max_length=5, unique=True, blank=True,
            help_text='<em>e.g. m</em><br />This will be used in printing instead of name if provided.')

    class Meta:
        verbose_name = 'unit of measure'
        verbose_name_plural = 'units of measure'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stocks_uom_detail', kwargs={'pk': self.pk})

    def get_printing_display(self):
        if self.abbreviation:
            return self.abbreviation
        else:
            return self.name


class Stock(models.Model):
    product = models.OneToOneField(Product)
    uom = models.ForeignKey(Uom, verbose_name='Unit of measure')

    class Meta:
        ordering = ['product']

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse('stocks_stock_detail', kwargs={'pk': self.pk})

    def total_amount(self):
        return LogEntry.objects.filter(log__stock=self).aggregate(Sum('amount'))['amount__sum']


class Warehouse(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stocks_warehouse_detail', kwargs={'pk': self.pk})

    def total_amount(self):
        return LogEntry.objects.filter(log__warehouse=self).aggregate(Sum('amount'))['amount__sum']


class Log(models.Model):
    stock = models.ForeignKey(Stock)
    warehouse = models.ForeignKey(Warehouse)

    class Meta:
        unique_together = ['stock', 'warehouse']
        ordering = ['stock', 'warehouse']

    def __str__(self):
        return '{} in {}'.format(self.stock, self.warehouse)

    def get_absolute_url(self):
        return reverse('stocks_log_detail', kwargs={'pk': self.pk})

    def total_amount(self):
        return self.logentry_set.all().aggregate(Sum('amount'))['amount__sum']


class LogEntry(models.Model):
    log = models.ForeignKey(Log)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    amount = models.IntegerField(help_text='Changes to the amount. Negative value for stock moving out. Positive value for stocks moving in.')

    def __str__(self):
        return '{} in {}'.format(self.created_at, self.log)
