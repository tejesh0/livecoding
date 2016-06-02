from __future__ import unicode_literals

from django.db import models

# Create your models here.


class GroupMember(models.Model):
    profile_id = models.CharField(max_length=180, unique=True)
    name = models.CharField(max_length=180)
    group_id = models.CharField(max_length=180)
    is_admin = models.BooleanField(default=False)

    def profile_url(self):
        return 'https://facebook.com/' + self.profile_id
