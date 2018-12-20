# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 07:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0003_auto_20181220_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
