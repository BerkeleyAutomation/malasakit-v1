# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-02 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0069_auto_20180202_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='respondent',
            name='sector',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]