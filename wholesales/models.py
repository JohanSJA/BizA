from django.db import models

from partners.models import Partner


class Salesman(models.Model):
    code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'salesmen'

    def __str__(self):
        return self.name


class Customer(models.Model):
    partner = models.OneToOneField(Partner)
    code = models.CharField(max_length=15, unique=True)
    served_by = models.ForeignKey(Salesman)

    def __str__(self):
        return str(self.partner)
