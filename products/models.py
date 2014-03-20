from django.db import models
from django.core.urlresolvers import reverse


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
