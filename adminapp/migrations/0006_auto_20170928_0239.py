# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-28 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_auto_20170926_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='foto',
            field=models.ImageField(upload_to='fotos_articulos/'),
        ),
    ]
