from django.db import models

from django.core.exceptions import ValidationError, ObjectDoesNotExist

from products.models import Product


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
