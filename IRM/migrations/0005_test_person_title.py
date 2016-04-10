# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-06 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IRM', '0004_auto_20160406_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_person',
            name='Title',
            field=models.ForeignKey(default=1, help_text='Title', on_delete=django.db.models.deletion.CASCADE, to='IRM.IRM_Title', verbose_name='Title'),
            preserve_default=False,
        ),
    ]