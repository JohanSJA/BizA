from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User)
    admission_date = models.DateField()
    registry_number = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user.get_username()
