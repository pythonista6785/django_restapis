# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-28 06:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status post', 'verbose_name_plural': 'Status posts'},
        ),
    ]
