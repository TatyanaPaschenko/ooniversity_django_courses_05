# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-09 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
