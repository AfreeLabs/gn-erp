# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-03 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departement', '0005_courselevel_course'),
        ('admission', '0003_registration_course_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='departement.Course'),
            preserve_default=False,
        ),
    ]
