from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Company(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Team(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company)
