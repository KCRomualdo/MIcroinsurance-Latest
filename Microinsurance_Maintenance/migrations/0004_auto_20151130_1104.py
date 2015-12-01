# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Microinsurance_Maintenance', '0003_auto_20151130_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('firstName', models.CharField(max_length=50, verbose_name=' *  First Name:')),
                ('midName', models.CharField(max_length=50, blank='true', verbose_name=' Middle Name:')),
                ('lastName', models.CharField(max_length=50, verbose_name=' *  Last Name:')),
                ('contactNo', models.CharField(max_length=20, verbose_name=' *  Contact Number:')),
                ('user_branch', models.ForeignKey(default='', verbose_name=' *  Assign branch:', to='Microinsurance_Maintenance.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('userTypeName', models.CharField(default='', max_length=50, verbose_name=' *  User Type:')),
            ],
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='personnel_branch',
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='personnel_ptype',
        ),
        migrations.DeleteModel(
            name='Personnel',
        ),
        migrations.DeleteModel(
            name='PersonnelType',
        ),
        migrations.AddField(
            model_name='user',
            name='user_ptype',
            field=models.ForeignKey(default='', verbose_name=' *  User type:', to='Microinsurance_Maintenance.UserType'),
        ),
    ]
