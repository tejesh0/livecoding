# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0004_auto_20160530_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordsearchsuggest',
            name='last_tweet_id',
            field=models.CharField(default=735995137705316353, max_length=100),
            preserve_default=False,
        ),
    ]