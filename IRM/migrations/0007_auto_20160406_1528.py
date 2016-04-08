# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IRM', '0006_irm_agency_admin_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='irm_agency_admin_contact',
            name='Mobile',
            field=models.CharField(blank=True, help_text='Mobile Number', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='irm_agency_admin_contact',
            name='Notes',
            field=models.TextField(blank=True, help_text='Short Notes about Agency', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='irm_agency_admin_contact',
            name='Phone',
            field=models.CharField(blank=True, help_text='Phone Number', max_length=200, null=True),
        ),
    ]
