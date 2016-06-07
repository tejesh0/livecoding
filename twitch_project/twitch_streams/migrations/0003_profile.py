# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-05 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitch_streams', '0002_auto_20160524_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, unique=True)),
                ('channel_id', models.IntegerField()),
                ('status', models.TextField()),
                ('views', models.IntegerField()),
                ('followers', models.IntegerField()),
                ('url', models.URLField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('game', models.CharField(blank=True, max_length=200, null=True)),
                ('broadcaster_language', models.CharField(blank=True, max_length=10, null=True)),
                ('is_already_reviewed', models.BooleanField(default=False)),
            ],
        ),
    ]