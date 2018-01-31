# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-01-01 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_auto_20180101_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportAdministrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('functional_group', models.CharField(choices=[('Servicedesk', 'Servicedesk'), ('IT-Projects', 'IT-Projects'), ('IT-Support', 'IT-Support'), ('Personnel', 'Personnel'), ('Finance', 'Finance'), ('Finance', 'Finance'), ('Marketing', 'Marketing')], max_length=25)),
                ('functional_subgroup', models.CharField(max_length=75)),
                ('administrator', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='assigned_admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.SupportAdministrator'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_category',
            field=models.CharField(choices=[('CRM', 'CRM'), ('IT', 'IT'), ('Finance', 'Finance'), ('HR', 'HR'), ('Others', 'Others')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ticketmanager',
            name='ticket_manager_fg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.SupportAdministrator'),
        ),
        migrations.DeleteModel(
            name='HelpDeskManager',
        ),
    ]
