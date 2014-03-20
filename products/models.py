from django.db import models
from django.core.urlresolvers import reverse


class Uom(models.Model):
    name = models.CharField(max_length=50, unique=True,
            help_text='<em>e.g. meter</em>')
    abbreviation = models.CharField(max_length=5, blank=True,
            help_text='<em>e.g. m</em><br />This will be used in printing instead of name if provided.')

    class Meta:
        verbose_name = 'unit of measure'
        verbose_name_plural = 'units of measure'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_uom_detail', kwargs={'pk': self.pk})

    def get_printing_display(self):
        if self.abbreviation:
            return self.abbreviation
        else:
            return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_category_detail', kwargs={'pk': self.pk})


class Product(models.Model):
    code = models.CharField(max_length=10, unique=True,
            help_text='Unique code to identify the product.')
    name = models.CharField(max_length=50, unique=True,
            help_text='Unique name to identify the product.')
    description = models.CharField(max_length=200, blank=True,
            help_text='This will be used in printing instead of name if provided.')
    category = models.ForeignKey(Category)
    uom = models.ForeignKey(Uom, verbose_name='unit of measure')
    note = models.TextField(blank=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_product_detail', kwargs={'pk': self.pk})

    def get_printing_display(self):
        if self.description:
            return self.description
        else:
            return self.name
