# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_bot', '0003_auto_20160604_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubedata',
            name='channel_id',
            field=models.CharField(blank=True, max_length=240, null=True, unique=True),
        ),
    ]
