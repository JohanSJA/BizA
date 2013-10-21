from django.db import models
from django.core.urlresolvers import reverse

class Warehouse(models.Model):
    name = models.CharField(max_length=32)
    location = models.TextField()

    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=32, unique=True)
    barcode = models.CharField(max_length=12, unique=True)
    retail_price = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    lowest_retail_price = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    wholesale_price = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    lowest_wholesale_price = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stocks_product_detail', kwargs={'pk': self.pk})

    def is_package(self):
        try:
            self.package
            return True
        except Package.DoesNotExist, e:
            return False

class Item(Product):
    cost_price = models.DecimalField(max_digits=12, decimal_places=4)

class ItemQuantity(models.Model):
    item = models.ForeignKey(Item)
    warehouse = models.ForeignKey(Warehouse)
    quantity = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'item quantities'

    def __unicode__(self):
        return '{} {} at {} on {}'.format(self.quantity, self.item, self.warehouse, self.datetime)

class Package(Product):

    def cost_price(self):
        cost = 0
        for pkgitem in self.packageitem_set.all():
            cost += pkgitem.quantity * pkgitem.item.cost_price
        return cost

    def separate_retail_price(self):
        price = 0
        for pkgitem in self.packageitem_set.all():
            price += pkgitem.quantity * pkgitem.item.retail_price
        return price

    def separate_wholesale_price(self):
        price = 0
        for pkgitem in self.packageitem_set.all():
            price += pkgitem.quantity * pkgitem.item.wholesale_price
        return price

class PackageItem(models.Model):
    package = models.ForeignKey(Package)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ['package', 'item']
