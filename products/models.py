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


class Pricelist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    base = models.ForeignKey("self", null=True, blank=True)
    base_derivation = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.base == self:
            raise ValidationError("Base couldn't be itself.")
        if self.base:
            if self.base.base:
                raise ValidationError("Base couldn't have a base.")
            if not self.base_derivation:
                raise ValidationError("Base derivation is needed when base is selected.")
        else:
            if self.base_derivation:
                raise ValidationError("Base derivation is not needed when base is not selected.")


class PricelistEntry(models.Model):
    pricelist = models.ForeignKey(Pricelist)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        unique_together = ["pricelist", "product"]

    def __str__(self):
        return "{} in {}".format(self.product, self.pricelist)

    def clean(self):
        if self.pricelist.base:
            base_pricelist = self.pricelist.base
            try:
                base_entry = PricelistEntry.objects.get(pricelist=base_pricelist, product=self.product)
                lowest_accepted_price = base_entry.price * self.pricelist.base_derivation / 100
                if self.price < lowest_accepted_price:
                    raise ValidationError("Price has to be higher than {}.".format(lowest_accepted_price))
            except ObjectDoesNotExist:
                pass


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
