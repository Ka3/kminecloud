# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 07:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Theme_colour', models.CharField(choices=[('blue', 'blue'), ('orange', 'orange'), ('red', 'red'), ('light', 'light'), ('purple', 'purple'), ('aqua', 'aqua'), ('brown', 'brown'), ('dark-blue', 'dark-blue'), ('light-green', 'light-green'), ('dark-red', 'dark-red'), ('teal', 'teal')], default='blue', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
