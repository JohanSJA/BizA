from django.db import models

from django.contrib.auth.models import User
from retails.models import Store

class Employee(models.Model):
    user = models.OneToOneField(User)
    hq = models.BooleanField("HQ access")
    store = models.ForeignKey(Store, null=True, blank=True)

    def __unicode__(self):
        return self.user.get_username()

    def work_in_hq(self):
        if self.store:
            return False
        else:
            return True
