# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tureview', '0006_auto_20180111_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='course',
        ),
        migrations.AddField(
            model_name='timeslot',
            name='course',
            field=models.ForeignKey(default='2ID60', on_delete=django.db.models.deletion.CASCADE, to='tureview.Course'),
            preserve_default=False,
        ),
    ]
