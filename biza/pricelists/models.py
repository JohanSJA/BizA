from django.db import models


class Pricelist(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    base_pricelist = models.ForeignKey('self', null=True, blank=True,
            help_text='pricelist to be used, if product not found on this pricelist.')
    is_tax_included = models.BooleanField(default=False)
    is_so_pricelist = models.BooleanField(default=True,
            help_text='this is a sales pricelist')
    enforce_price_limit = models.BooleanField(default=False,
            help_text='do not allow prices below the limit price')
    price_precision = models.SmallIntegerField(default=2,
            help_text='precision (number of decimals) for the price')

    def __unicode__(self):
        return self.name
