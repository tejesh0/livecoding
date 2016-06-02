from __future__ import unicode_literals

from django.db import models

# Create your models here.


class YoutubeSearchFilters(models.Model):
    search_term = models.CharField(max_length=40)
    location = models.CharField(max_length=40, help_text="add latitude, longitude coordinates", default="37.42307,-122.08427")
    location_radius = models.CharField(max_length=10, help_text="Example: 5mi, 10km", default="20km")
    max_results = models.PositiveIntegerField(default=25)
    eventType = models.CharField(max_length=10, default="completed")
    order = models.CharField(max_length=15, default="viewCount")

# class YoutubeData(models.Model):
# 