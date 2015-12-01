# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0005_auto_20151130_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('c_firstName', models.CharField(max_length=50, verbose_name=' *  First Name:')),
                ('c_middleName', models.CharField(max_length=50, verbose_name=' *  Middle Name:', blank='true')),
                ('c_lastName', models.CharField(max_length=50, verbose_name=' *  Last Name:')),
                ('c_phoneNumber', models.CharField(max_length=20, verbose_name=' *  Contact Number:')),
            ],
        ),
    ]
