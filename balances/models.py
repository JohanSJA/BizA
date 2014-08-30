from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Sum

from products.models import Product


class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products_warehouse_detail", kwargs={"pk": self.pk})

    def balance(self):
        summary = BalanceLogEntry.objects.filter(balance_log__warehouse=self).aggregate(Sum("amount"))
        if summary["amount__sum"]:
            return summary["amount__sum"]
        else:
            return 0


class BalanceLog(models.Model):
    product = models.ForeignKey(Product)
    warehouse = models.ForeignKey(Warehouse)

    class Meta:
        unique_together = ["product", "warehouse"]

    def __str__(self):
        return "{} at {}".format(self.product, self.warehouse)

    def get_absolute_url(self):
        return reverse("products_balancelog_detail", kwargs={"pk": self.pk})

    def total_amount(self):
        summary = self.balancelogentry_set.aggregate(Sum("amount"))
        return summary["amount__sum"]


class BalanceLogEntry(models.Model):
    balance_log = models.ForeignKey(BalanceLog)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    amount = models.IntegerField()

    class Meta:
        verbose_name_plural = "balance log entries"

    def __str__(self):
        return "{} at {}".format(self.amount, self.timestamp)
