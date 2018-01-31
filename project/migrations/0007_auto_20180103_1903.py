# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-03 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20180103_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectrisk',
            name='projectName',
        ),
        migrations.AddField(
            model_name='projectrisk',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.Ldrproject'),
        ),
    ]
