# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-10 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargarEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ide', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
            ],
        ),
    ]
