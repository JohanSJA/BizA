from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    partner = models.ForeignKey(Partner)
    function = models.CharField(max_length=50)
    address = models.TextField()

    class Meta:
        unique_together = ['partner', 'function']

    def __str__(self):
        return '{} - {}'.format(str(self.partner), self.function)


class ContactMethod(models.Model):
    METHODS = [
        ('tel', 'Telephone'),
        ('fax', 'Fax'),
        ('email', 'E-mail'),
    ]

    partner = models.ForeignKey(Partner)
    method = models.CharField(max_length=10, choices=METHODS)
    information = models.CharField(max_length=50)

    def __str__(self):
        return '{} - {}'.format(str(self.partner), self.method)
