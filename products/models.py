from django.db import models
from django.core.urlresolvers import reverse


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
    uom = models.ForeignKey(Uom, verbose_name="unit of measurement")
    remark = models.TextField(blank=True)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("products_product_detail", kwargs={"pk": self.pk})

    def balance(self):
        summary = BalanceLogEntry.objects.filter(balance_log__product=self).aggregate(Sum("amount"))
        return summary["amount__sum"]


class Pricelist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    base = models.ForeignKey("self", null=True, blank=True)
    base_derivation = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products_pricelist_detail", kwargs={"pk": self.pk})


class PricelistEntry(models.Model):
    pricelist = models.ForeignKey(Pricelist)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        unique_together = ["pricelist", "product"]

    def __str__(self):
        return "{} in {}".format(self.product, self.pricelist)


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.id

    def balance(self):
        summary = BalanceLogEntry.objects.filter(balance_log__warehouse=self).aggregate(Sum("amount"))
        return summary["amount__sum"]


class BalanceLog(models.Model):
    product = models.ForeignKey(Product)
    warehouse = models.ForeignKey(Warehouse)

    class Meta:
        unique_together = ["product", "warehouse"]

    def __str__(self):
        return "{} at {}".format(self.product, self.warehouse)

    def total_amount(self):
        summary = self.balancelogentry_set.aggregate(Sum("amount"))
        return summary["amount__sum"]


class BalanceLogEntry(models.Model):
    balance_log = models.ForeignKey(BalanceLog)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return "{} at {}".format(self.amount, self.timestamp)
