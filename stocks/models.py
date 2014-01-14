from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=3, unique=True)

    def __unicode__(self):
        return self.abbreviation


class Stock(models.Model):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    unit = models.ForeignKey(Unit)
    discontinued = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField()

    def __unicode__(self):
        return self.name


class Balance(models.Model):
    stock = models.ForeignKey(Stock)
    warehouse = models.ForeignKey(Warehouse)
    changes = models.IntegerField()
    amount = models.IntegerField()

    def __unicode__(self):
        return '{} {} in {}'.format(self.amount, self.stock, self.warehouse)
