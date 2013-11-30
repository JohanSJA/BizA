from django.db import models

from branches.models import Branch


class Drawer(models.Model):
    branch = models.ForeignKey(Branch)
    name = models.CharField(max_length=50)

    class Meta:
        unique_together = ('branch', 'name')

    def __unicode__(self):
        return '{} {}'.format(self.branch, self.name)

class Session(models.Model):
    drawer = models.ForeignKey(Drawer)
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField(null=True, blank=True)
    initial_cash_amount = models.DecimalField(max_digits=20, decimal_places=2)
    final_cash_amount = models.DecimalField(max_digits=20, decimal_places=2,
            null=True, blank=True)
    status = models.SmallIntegerField()

    def __unicode__(self):
        return '{} {}'.format(self.station, self.opening_time)
