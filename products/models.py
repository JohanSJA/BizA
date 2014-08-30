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
    barcode = models.CharField(max_length=20, blank=True)
    remark = models.TextField(blank=True)

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("products_product_detail", kwargs={"pk": self.pk})
