# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 01:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grumblr', '0008_auto_20161002_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='follow',
            field=models.ManyToManyField(related_name='FOLLOW', to=settings.AUTH_USER_MODEL),
        ),
    ]
