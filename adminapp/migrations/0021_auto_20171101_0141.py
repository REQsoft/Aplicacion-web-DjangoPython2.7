# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-01 01:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0020_parametrizacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parametrizacion',
            old_name='estado_articulos',
            new_name='estado_articulo',
        ),
        migrations.RenameField(
            model_name='parametrizacion',
            old_name='estado_servicios',
            new_name='estado_servicio',
        ),
    ]
