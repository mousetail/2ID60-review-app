# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tureview', '0009_course_averagerating'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='reviewNumber',
            field=models.IntegerField(default=0),
        ),
    ]
