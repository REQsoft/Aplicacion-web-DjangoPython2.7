# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-05 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0036_sql'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sql',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]