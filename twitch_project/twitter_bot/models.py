from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LivecodingHandle(models.Model):
    keyword = models.CharField(max_length=40)
    minimum_retweets = models.PositiveSmallIntegerField(default=0)
    minimum_likes = models.PositiveSmallIntegerField(default=0)
    last_tweet_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'favorite search result'
        verbose_name_plural = 'favorite search results'


class KeywordSearchSuggest(models.Model):
    include_words = models.CharField(max_length=140)
    exclude_words = models.CharField(max_length=140, blank=True)
    minimum_retweets = models.PositiveSmallIntegerField(default=10)
    minimum_likes = models.PositiveSmallIntegerField(default=20)
    last_tweet_id = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'retweet and favorite result'
        verbose_name_plural = 'retweet and favorite results'


class Credentials(models.Model):
    access_token = models.CharField(max_length=240)
    access_token_secret = models.CharField(max_length=240)
    consumer_secret = models.CharField(max_length=240)
    consumer_key = models.CharField(max_length=240)

    class Meta:
        verbose_name = 'credentials'
        verbose_name_plural = 'credentials'


class FollowFollowersOfAccount(models.Model):
    screen_name = models.CharField(max_length=140, unique=True)
    is_accounts_followed = models.BooleanField(default=False)
