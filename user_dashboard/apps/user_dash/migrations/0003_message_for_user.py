# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_dash', '0002_auto_20170924_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='for_user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='wall_msgs', to='user_dash.User'),
            preserve_default=False,
        ),
    ]
