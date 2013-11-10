from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=32)
    prefix = models.CharField(max_length=5)
    length = models.SmallIntegerField()

    def __unicode__(self):
        return self.name


class Version(models.Model):
    document = models.OneToOneField(Document)
    number = models.IntegerField(default=1)

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self, next=False):
        padding_length = self.document.length - len(self.document.prefix) - len(str(self.number))
        padding = '0' * padding_length
        return '{}{}{}'.format(self.document.prefix, padding, self.number)

    def get_next(self):
        return self.get_full_name(next=True)
