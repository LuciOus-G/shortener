# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-02 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_url', '0008_auto_20200203_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short',
            name='link',
            field=models.CharField(blank=True, default='Link', max_length=255, unique=True),
        ),
    ]
