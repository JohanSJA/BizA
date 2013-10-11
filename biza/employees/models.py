from django.db import models

from django.contrib.auth.models import User
from retails.models import Store

class Employee(models.Model):
    user = models.OneToOneField(User)
    store = models.ForeignKey(Store, null=True, blank=True)
