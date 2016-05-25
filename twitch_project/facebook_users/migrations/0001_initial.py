# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.CharField(max_length=180, unique=True)),
                ('name', models.CharField(max_length=180)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]