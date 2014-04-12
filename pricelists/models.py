from django.db import models

from products.models import Product


class Pricelist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    base = models.ForeignKey("self", null=True, blank=True)
    base_derivation = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class PricelistEntry(models.Model):
    pricelist = models.ForeignKey(Pricelist)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        unique_together = ["pricelist", "product"]

    def __str__(self):
        return "{} in {}".format(self.product, self.pricelist)
