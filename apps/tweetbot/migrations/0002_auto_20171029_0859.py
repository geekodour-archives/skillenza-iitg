# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractedtweet',
            name='tweetid',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='extracteduser',
            name='userid',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
