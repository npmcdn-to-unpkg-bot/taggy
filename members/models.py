from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Team(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Group(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team)


class MemberRole(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Member(models.Model):
    user = models.OneToOneField(User)
    public_key = models.TextField()
    private_key = models.TextField()
    teams = models.ManyToManyField(Team, through='TeamMember')
    groups = models.ManyToManyField(Group, through='GroupMember')


class TeamMember(models.Model):
    team = models.ForeignKey(Team)
    member = models.ForeignKey(Member)
    role = models.ForeignKey(MemberRole)


class GroupMember(models.Model):
    group = models.ForeignKey(Group)
    member = models.ForeignKey(Member)
    role = models.ForeignKey(MemberRole)

