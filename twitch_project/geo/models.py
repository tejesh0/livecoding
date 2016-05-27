from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Geo(models.Model):
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    address = models.TextField()
