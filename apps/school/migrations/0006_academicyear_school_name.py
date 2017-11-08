# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_remove_academicyear_school_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicyear',
            name='school_name',
            field=models.ForeignKey(default=5456, on_delete=django.db.models.deletion.CASCADE, to='school.School'),
            preserve_default=False,
        ),
    ]