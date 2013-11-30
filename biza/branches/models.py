from django.db import models

from employees.models import Employee


class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'branches'

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    branch = models.ForeignKey(Branch)
    employee = models.ForeignKey(Employee, unique=True)

    def __unicode__(self):
        return '{} {}'.format(self.branch, self.employee)
