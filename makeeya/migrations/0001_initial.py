# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-14 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, upload_to='Buyer/')),
                ('original_Price', models.IntegerField()),
                ('current_price', models.IntegerField()),
                ('expiry_date', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeeya.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_description', tinymce.models.HTMLField()),
                ('business_logo', models.ImageField(blank=True, upload_to='Buyer/')),
                ('business_email', models.EmailField(max_length=254)),
                ('business_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_identification_number', models.CharField(max_length=100)),
                ('prefered_username', models.CharField(max_length=100)),
                ('business_phone_number', models.IntegerField()),
                ('business_email', models.EmailField(max_length=254)),
                ('Business_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='makeeya.Request'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeeya.Profile'),
        ),
    ]
