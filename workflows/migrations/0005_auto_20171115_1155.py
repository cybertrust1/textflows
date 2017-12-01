# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-11-15 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0004_auto_20161122_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractwidget',
            name='has_file',
            field=models.BooleanField(default=False, help_text=b'The has file flag is currently under construction, please do not use it yet.'),
        ),
        migrations.AlterField(
            model_name='abstractinput',
            name='parameter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='abstractinput',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='input',
            name='parameter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='input',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]