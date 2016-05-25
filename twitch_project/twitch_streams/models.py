from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Streamer(models.Model):
    name = models.CharField(max_length=180, unique=True)
    channel_id = models.IntegerField()
    status = models.TextField()
