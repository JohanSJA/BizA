from django.db import models

from common.models import Product


class PriceList(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    price_list = models.ForeignKey(PriceList)
    product = models.ForeignKey(Product)
    standard_price = models.DecimalField(max_digits=12, decimal_places=4)
    lowest_price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        unique_together = ('price_list', 'product')

    def __str__(self):
        return 'Product {} in price list {}'.format(self.product, self.price_list)
