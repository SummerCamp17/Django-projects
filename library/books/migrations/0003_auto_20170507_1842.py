# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-07 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170507_1834'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
