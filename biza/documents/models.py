from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=32)
    prefix = models.CharField(max_length=5)
    length = models.SmallIntegerField()
    number = models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

    def get_full_name(self, next=False):
        padding_length = self.length - len(self.prefix) - len(str(self.number))
        padding = '0' * padding_length
        if next:
            number = self.number + 1
        else:
            number = self.number
        return '{}{}{}'.format(self.prefix, padding, number)
