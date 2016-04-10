# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IRM', '0007_auto_20160406_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='irm_agency',
            name='AgencyFullName',
        ),
        migrations.RemoveField(
            model_name='irm_agency',
            name='AgencyName',
        ),
        migrations.AddField(
            model_name='irm_agency',
            name='Agency_FullName',
            field=models.CharField(blank=True, help_text='Agency Full Name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='irm_agency',
            name='Agency_Name',
            field=models.CharField(blank=True, help_text='Agency Name', max_length=100, null=True),
        ),
    ]