from django.db import models

from branches.models import Station


class Till(models.Model):
    station = models.ForeignKey(Station)
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField(null=True, blank=True)
    initial_cash_amount = models.DecimalField(max_digits=20, decimal_places=2)
    final_cash_amount = models.DecimalField(max_digits=20, decimal_places=2,
            null=True, blank=True)
    status = models.SmallIntegerField()

    def __unicode__(self):
        return '{} {}'.format(self.station, self.opening_time)

class Entry(models.Model):
    till = models.ForeignKey(Till)
    time = models.DateTimeField()
    value = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return '{} {}'.format(self.till, self.time)
