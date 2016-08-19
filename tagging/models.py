from __future__ import unicode_literals

from django.db import models
from members.models import Team


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    team = models.ForeignKey(Team)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    team = models.ForeignKey(Team)


class Taggable(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.name
