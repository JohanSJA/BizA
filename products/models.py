from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=12, unique=True)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    remark = models.TextField(blank=True)

    def __str__(self):
        return self.code
