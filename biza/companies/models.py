from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    reg_num = models.CharField('registration number', max_length=16, unique=True)
    address = models.TextField()
    tel = models.CharField('telephone', max_length=16, unique=True)
    fax = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'companies'
        ordering = ['name']

    def __unicode__(self):
        return '{} ({})'.format(self.name, self.reg_num)
