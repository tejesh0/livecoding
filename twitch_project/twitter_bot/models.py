from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LivecodingHandle(models.Model):
    keyword = models.CharField(max_length=40)
    minimum_retweets = models.PositiveSmallIntegerField(default=0)
    minimum_likes = models.PositiveSmallIntegerField(default=0)
    last_tweet_id = models.CharField(max_length=100)


class KeywordSearchSuggest(models.Model):
    include_words = models.CharField(max_length=140)
    exclude_words = models.CharField(max_length=140, blank=True)
    minimum_retweets = models.PositiveSmallIntegerField(default=10)
    minimum_likes = models.PositiveSmallIntegerField(default=20)
    last_tweet_id = models.CharField(max_length=100)
