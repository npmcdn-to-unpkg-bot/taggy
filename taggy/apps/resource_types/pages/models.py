from __future__ import unicode_literals

from django.db import models
from taggy.apps.access.models import Team
from taggy.apps.tagging.models import Taggable


# Create your models here.
class ResourcePage(models.Model):
    taggable = models.OneToOneField(Taggable)
    content = models.TextField(blank=True)
