# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('promoName', models.CharField(max_length=50, verbose_name=' *  Promo Name:')),
                ('promoPrice', models.PositiveIntegerField(max_length=6, verbose_name=' *  New price:')),
                ('promoEffectivestartDate', models.DateField(verbose_name=' *  Start Date of the Promo:')),
                ('promoEffectiveendDate', models.DateField(verbose_name=' *  End Date of the Promo:')),
                ('promoInsurance', models.ForeignKey(to='Microinsurance_Maintenance.InsuranceOffer', verbose_name=' *  Insurance offer:', default='')),
            ],
        ),
    ]
