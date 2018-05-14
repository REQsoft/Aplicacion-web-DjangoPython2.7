# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-10-14 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0016_auto_20171010_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametrizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('eslogan', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='fotos_param')),
                ('informacion', models.CharField(max_length=200)),
            ],
        ),
    ]