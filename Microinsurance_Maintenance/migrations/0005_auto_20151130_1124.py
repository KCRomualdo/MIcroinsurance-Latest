# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0004_auto_20151130_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='emailAdd',
            field=models.CharField(verbose_name=' *  Email Address:', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='user_pword',
            field=models.CharField(verbose_name=' *  Password:', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='user_uname',
            field=models.CharField(verbose_name=' *  Username:', max_length=50, default=''),
        ),
    ]
