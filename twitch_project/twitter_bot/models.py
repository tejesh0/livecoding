from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LivecodingHandle(models.Model):
    keyword = models.CharField(max_length=40)
