from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Sum


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products_category_detail", kwargs={"pk": self.pk})


class Uom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=5, help_text="Used in printing")

    class Meta:
        verbose_name = "unit of measure"
        verbose_name_plural = "units of measure"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products_uom_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    model = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, help_text="Used in printing.")
    category = models.ForeignKey(Category)
    barcode = models.CharField(max_length=20, blank=True)
    remark = models.TextField(blank=True)

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("products_product_detail", kwargs={"pk": self.pk})

    def balance(self):
        summary = BalanceLogEntry.objects.filter(balance_log__product=self).aggregate(Sum("amount"))
        if summary["amount__sum"]:
            return summary["amount__sum"]
        else:
            return 0


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
