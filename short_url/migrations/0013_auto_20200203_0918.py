# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-03 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_url', '0012_content_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(choices=[('game', 'game'), ('crypto', 'crypto')], default='', max_length=255),
        ),
    ]
