from __future__ import unicode_literals

from django.db import models
from members.models import Team
from tagging.models import Tag


# Create your models here.
class ResourceSecret(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    team = models.ForeignKey(Team)
