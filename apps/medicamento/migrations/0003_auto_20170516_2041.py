# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-17 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0002_auto_20170516_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='estado',
            field=models.BooleanField(),
        ),
    ]
