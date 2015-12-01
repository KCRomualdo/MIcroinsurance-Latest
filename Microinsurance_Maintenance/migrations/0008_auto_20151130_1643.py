# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0007_auto_20151130_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avail',
            name='date_avail',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=' *  Date availed:'),
        ),
    ]
