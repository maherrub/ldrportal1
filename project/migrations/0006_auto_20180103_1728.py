# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-03 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20180103_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ldrprojectschedule',
            old_name='projectName',
            new_name='project',
        ),
        migrations.RemoveField(
            model_name='ldrprojectschedule',
            name='members',
        ),
        migrations.AddField(
            model_name='ldrscheduledactivity',
            name='members',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.Ldrresource'),
        ),
    ]
