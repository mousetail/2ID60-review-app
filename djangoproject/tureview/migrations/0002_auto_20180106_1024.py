# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tureview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course',
            new_name='teachers',
        ),
    ]
