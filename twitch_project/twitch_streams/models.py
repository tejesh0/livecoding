from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Streamer(models.Model):
    name = models.CharField(max_length=180, unique=True)
    channel_id = models.IntegerField()
    status = models.TextField()


class Profile(models.Model):
    name = models.CharField(max_length=180, unique=True)
    channel_id = models.IntegerField()
    status = models.TextField()
    views = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    game = models.CharField(max_length=200, blank=True, null=True)
    broadcaster_language = models.CharField(max_length=10, blank=True, null=True)
    is_already_reviewed = models.BooleanField(default=False)
