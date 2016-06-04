from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AccessToken(models.Model):
    access_token = models.CharField(max_length=140)
    user = models.OneToOneField(to=User)
