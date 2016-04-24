# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IRM', '0020_auto_20160412_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency_Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(help_text='Agency Decision', max_length=100, verbose_name='Agency Decision')),
            ],
        ),
        migrations.AlterField(
            model_name='case_type',
            name='types',
            field=models.CharField(help_text='Type of Case', max_length=100, verbose_name='Case_Type'),
        ),
        migrations.AlterField(
            model_name='irm_case',
            name='Agency_Decision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IRM.Agency_Decision'),
        ),
        migrations.AlterField(
            model_name='irm_case',
            name='Person_2_DateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='panel_recommendations',
            name='types',
            field=models.CharField(help_text='Panel Recommendations', max_length=100, verbose_name='Panel_Recommendations'),
        ),
        migrations.AlterField(
            model_name='report_status',
            name='types',
            field=models.CharField(help_text='Report Status', max_length=100, verbose_name='Report_Status'),
        ),
    ]