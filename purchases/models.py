from django.db import models

from partners.models import Partner


class Supplier(models.Model):
    partner = models.OneToOneField(Partner)
    code = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return str(self.partner)
