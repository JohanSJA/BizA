from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import Sum


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


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stocks_category_detail', kwargs={'pk': self.pk})


class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category)

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True,
            help_text='Will be used in printing if provided.')
    note = models.TextField(blank=True)

    uom = models.ForeignKey(Uom, verbose_name='Unit of measure')

    barcode = models.CharField(max_length=30, unique=True,
            blank=True, null=True)

    cost_price = models.DecimalField(max_digits=12, decimal_places=4,
            blank=True, null=True)
    wholesales_price = models.DecimalField(max_digits=12, decimal_places=4,
            blank=True, null=True)
    retail_price = models.DecimalField(max_digits=12, decimal_places=4,
            blank=True, null=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('stocks_product_detail', kwargs={'pk': self.pk})

    def total_amount(self):
        return LogEntry.objects.filter(log__stock=self).aggregate(Sum('amount'))['amount__sum']

    def get_printing_display(self):
        if self.description:
            return self.description
        else:
            return self.name


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
    product = models.ForeignKey(Product)
    warehouse = models.ForeignKey(Warehouse)

    class Meta:
        unique_together = ['product', 'warehouse']
        ordering = ['product', 'warehouse']

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
