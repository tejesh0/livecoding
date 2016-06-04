from __future__ import unicode_literals

from django.db import models

# Create your models here.


class YoutubeSearchFilters(models.Model):
    search_term = models.CharField(max_length=40)
    # location = models.CharField(max_length=40, help_text="add latitude, longitude coordinates", default="37.42307,-122.08427")
    # location_radius = models.CharField(max_length=10, help_text="Example: 5mi, 10km", default="20km")
    order = models.CharField(max_length=15, default="viewCount")


class YoutubeData(models.Model):
    comment_count = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    video_count = models.PositiveIntegerField(default=0)
    subscriber_count = models.PositiveIntegerField(default=0)
    google_plus_user_Id = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=240, blank=True, null=True)
    channel_id = models.CharField(max_length=240, blank=True, null=True)
    country = models.CharField(max_length=140, blank=True, null=True)
