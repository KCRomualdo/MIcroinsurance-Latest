# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0002_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='promoPrice',
            field=models.PositiveIntegerField(verbose_name=' *  New price:', default=0),
        ),
    ]
