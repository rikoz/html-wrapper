# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170815_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionfile',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Application'),
        ),
    ]