# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departement', '0005_courselevel_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselevel',
            name='code_level',
            field=models.CharField(max_length=16),
        ),
    ]
