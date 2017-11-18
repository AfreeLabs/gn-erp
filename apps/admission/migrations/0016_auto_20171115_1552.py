# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 15:52
from __future__ import unicode_literals

import apps.admission.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0015_auto_20171115_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissionprocess',
            name='payment_date',
            field=models.DateField(default='2000-10-10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='registration_fees_paid',
            field=models.DecimalField(decimal_places=2, default=200000, max_digits=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='registree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admission.Registration'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admission',
            name='matricule',
            field=models.CharField(default=apps.admission.models.student_number, editable=False, max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='registry_number',
            field=models.CharField(default=apps.admission.models.registration_number, editable=False, max_length=18, unique=True),
        ),
    ]