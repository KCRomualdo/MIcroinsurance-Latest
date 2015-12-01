# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0008_auto_20151130_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avail',
            name='policyNumber',
            field=models.IntegerField(verbose_name=' *  Policy Number:', editable='false'),
        ),
    ]
