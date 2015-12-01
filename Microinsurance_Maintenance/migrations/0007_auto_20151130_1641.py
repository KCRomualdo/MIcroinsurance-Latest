# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0006_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avail',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('policyNumber', models.IntegerField(verbose_name=' *  Policy Number:')),
                ('date_avail', models.DateField(default=datetime.date(2015, 11, 30), verbose_name=' *  Date availed:')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_middleName',
            field=models.CharField(blank='true', verbose_name='   Middle Name:', max_length=50),
        ),
        migrations.AddField(
            model_name='avail',
            name='customerName',
            field=models.ForeignKey(default='', to='Microinsurance_Maintenance.Customer', verbose_name=' *  Customer Name:'),
        ),
        migrations.AddField(
            model_name='avail',
            name='insurance_avail',
            field=models.ForeignKey(verbose_name=' *  Availed Insurance:', to='Microinsurance_Maintenance.InsuranceOffer'),
        ),
    ]
