# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-06 01:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_auto_20171005_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListarEstudiante',
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
