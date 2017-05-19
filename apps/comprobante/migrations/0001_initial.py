# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-28 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comprobante',
            fields=[
                ('idcomprobante', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=20)),
                ('total', models.FloatField()),
                ('idcliente', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
