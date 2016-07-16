from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)
