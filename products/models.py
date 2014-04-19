from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Uom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=5, help_text="Used in printing")

    class Meta:
        verbose_name = "unit of measure"
        verbose_name_plural = "units of measure"

    def __str__(self):
        return self.name


class Product(models.Model):
    model = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, help_text="Used in printing.")
    category = models.ForeignKey(Category)
    uom = models.ForeignKey(Uom)
    remark = models.TextField(blank=True)

    def __str__(self):
        return self.model

    def balance(self):
        summary = LogEntry.objects.filter(log__warehouse=self).aggregate(Sum("amount"))
        return summary["amount__sum"]


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.id

    def balance(self):
        summary = LogEntry.objects.filter(log__warehouse=self).aggregate(Sum("amount"))
        return summary["amount__sum"]


class Log(models.Model):
    product = models.ForeignKey(Product)
    warehouse = models.ForeignKey(Warehouse)

    class Meta:
        unique_together = ["product", "warehouse"]

    def __str__(self):
        return "{} at {}".format(self.product, self.warehouse)

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
