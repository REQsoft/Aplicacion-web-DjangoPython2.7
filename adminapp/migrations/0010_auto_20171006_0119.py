# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-06 01:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_listarestudiante'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListarEstudiante',
            new_name='Estudiante',
        ),
    ]
