# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='car_ratings',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cars',
            name='car_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cars',
            name='car_year',
            field=models.IntegerField(),
        ),
    ]