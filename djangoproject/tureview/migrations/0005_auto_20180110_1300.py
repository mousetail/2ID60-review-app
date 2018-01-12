# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tureview', '0004_auto_20180110_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='faculty',
            field=models.CharField(choices=[('BMT', 'Biomedishe Technologie'), ('BK', 'Bouwkunde'), ('ESoE', 'Eindhoven School of Education'), ('EE', 'Electrical Engineering'), ('ID', 'Industrial Design'), ('IEID', 'Industrial Engineering & Innovation Sciences'), ('ST', 'Scheikundige Technologie'), ('TN', 'Technishe Natuurkunde'), ('wbtk', 'Werktuigboukunde'), ('WI', 'Wiskunde & Informatica')], default='BK', max_length=4),
        ),
    ]
