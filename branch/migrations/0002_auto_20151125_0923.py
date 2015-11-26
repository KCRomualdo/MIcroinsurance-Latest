# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='id_number',
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_name',
            field=models.CharField(default='Any branch', max_length=500),
        ),
    ]
