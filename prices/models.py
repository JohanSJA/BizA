from django.db import models

from products.models import Product


class Pricelist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    markup_from = models.ForeignKey('self', null=True, blank=True,
            help_text='Which pricelist to look for to perform markup.')
    markup_percentage = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class PricelistEntry(models.Model):
    pricelist = models.ForeignKey(Pricelist)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        unique_together = ['pricelist', 'product']

    def __str__(self):
        return '{} in {}'.format(self.product, self.pricelist)
