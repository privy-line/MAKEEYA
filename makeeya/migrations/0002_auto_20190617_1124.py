# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-17 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeeya', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='business_name',
            field=models.CharField(max_length=300),
        ),
    ]
