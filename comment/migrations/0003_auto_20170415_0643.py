# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20170415_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
