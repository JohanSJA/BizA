from django.db import models
from django.db.models import Sum

from products.models import Product


class Uom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=5, help_text="Name to be used during printing")

    class Meta:
        verbose_name = "unit of measure"
        verbose_name_plural = "units of measure"

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.OneToOneField(Product)
    uom = models.ForeignKey(Uom)

    def __str__(self):
        return str(self.product)

    def balance(self):
        summary = LogEntry.objects.filter(log__stock=self).aggregate(Sum("amount"))
        return summary["amount__sum"]


class Warehouse(models.Model):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.code

    def balance(self):
        summary = LogEntry.objects.filter(log__warehouse=self).aggregate(Sum("amount"))
        return summary["amount__sum"]


class Log(models.Model):
    stock = models.ForeignKey(Stock)
    warehouse = models.ForeignKey(Warehouse)

    class Meta:
        unique_together = ["stock", "warehouse"]

    def __str__(self):
        return "{} at {}".format(self.stock, self.warehouse)

    def balance(self):
        summary = self.logentry_set.aggregate(Sum("amount"))
        return summary["amount__sum"]


class LogEntry(models.Model):
    log = models.ForeignKey(Log)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return "{} at {}".format(self.amount, self.timestamp)
