# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-16 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa', '0002_auto_20190116_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hood',
            options={'ordering': ['hood_name']},
        ),
        migrations.AlterField(
            model_name='hood',
            name='occupants_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
