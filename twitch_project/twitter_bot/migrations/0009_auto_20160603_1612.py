# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 16:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0008_credentials'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credentials',
            options={'verbose_name': 'credentials', 'verbose_name_plural': 'credentials'},
        ),
    ]
