from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=32)
    barcode = models.CharField(max_length=12)
    retail_price = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    lowest_retail_price = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    wholesale_price = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    lowest_wholesale_price = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)

class Item(Product):
    cost_price = models.DecimalField(max_digits=12, decimal_places=4)

class Package(Product):
    pass

class PackageItem(models.Model):
    package = models.ForeignKey(Package)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ['package', 'item']
