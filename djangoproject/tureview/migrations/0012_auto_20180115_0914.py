# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-15 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tureview', '0011_auto_20180112_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ratingDiff',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='ratingInf',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='ratingRele',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='review',
            name='ratingTime',
            field=models.IntegerField(default=5),
        ),
    ]