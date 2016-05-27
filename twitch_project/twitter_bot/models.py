from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LivecodingHandle(models.Model):
    keyword = models.CharField(max_length=40)


class KeywordSearchSuggest(models.Model):
    include_words = models.CharField(max_length=140)
    exclude_words = models.CharField(max_length=140)
