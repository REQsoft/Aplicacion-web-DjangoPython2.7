# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-06 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_delete_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('contrasenia', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('port', models.CharField(max_length=100)),
                ('bd', models.CharField(max_length=100)),
                ('sql', models.CharField(max_length=100)),
                ('prueba', models.CharField(max_length=100)),
            ],
        ),
    ]
