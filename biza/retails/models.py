from django.db import models

from stocks.models import Warehouse, Product

class Store(models.Model):
    name = models.CharField(max_length=32)
    location = models.TextField(unique=True)
    warehouse = models.ForeignKey(Warehouse)
    
    def __unicode__(self):
        return self.name

class Saleperson(models.Model):
    name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name

class Sale(models.Model):
    store = models.ForeignKey(Store)
    saleperson = models.ForeignKey(Saleperson)
    open_time = models.DateTimeField(auto_now_add=True)
    closing_time = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return '{} at {}'.format(self.open_time, self.store)
        
    def total_amount(self):
        amount = 0
        for line in self.saleline_set.all():
            if line.discount:
                amount += line.quantity * (line.product.retail_price - line.discount)
            else:
                amount += line.quantity * line.product.retail_price
        return amount
    
class SaleLine(models.Model):
    sale = models.ForeignKey(Sale)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    
    class Meta:
        unique_together = ['sale', 'product']
    
    def __unicode__(self):
        return '{} {} in {}'.format(self.quantity, self.product, self.sale)
