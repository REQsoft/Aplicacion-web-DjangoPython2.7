# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-06 01:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_auto_20171006_0119'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]