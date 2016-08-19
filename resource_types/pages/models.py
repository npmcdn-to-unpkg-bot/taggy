from __future__ import unicode_literals

from django.db import models
from members.models import Team
from tagging.models import Taggable


# Create your models here.
class ResourcePage(models.Model):
    taggable = models.OneToOneField(Taggable)
    content = models.TextField(blank=True)
