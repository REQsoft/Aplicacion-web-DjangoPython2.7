# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-04 04:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0029_auto_20171104_0354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parametrizacion',
            old_name='informacion_asignatura',
            new_name='informacion_materia',
        ),
    ]
