# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170314_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='longitude',
            new_name='lon',
        ),
    ]
