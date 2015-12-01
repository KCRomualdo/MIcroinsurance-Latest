# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('branch_name', models.CharField(max_length=50, default='', verbose_name=' *  Branch name:')),
                ('branch_address', models.TextField(default='', verbose_name=' *  Branch address:')),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='InsuranceOffer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('SKU_name', models.CharField(max_length=50, default='', verbose_name=' *  SKU name:')),
                ('base_price', models.PositiveIntegerField(default=0, verbose_name=' *  Base price of SKU:')),
                ('selling_price', models.PositiveIntegerField(default=0, verbose_name=' *  Selling price of SKU:')),
                ('Valid_days', models.PositiveIntegerField(default=0, verbose_name=' *  Number of valid days:')),
                ('Age_range_from', models.PositiveIntegerField(default=0, verbose_name=' *  Age from:')),
                ('Age_range_to', models.PositiveIntegerField(default=0, verbose_name=' *  Age to:')),
                ('Limit_per_person', models.PositiveIntegerField(default=0, verbose_name=' *  Number of limit for availing this SKU:')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50, verbose_name=' *  First Name:')),
                ('midName', models.CharField(max_length=50, blank='true', verbose_name=' Middle Name:')),
                ('lastName', models.CharField(max_length=50, verbose_name=' *  Last Name:')),
                ('contactNo', models.CharField(max_length=20, verbose_name=' *  Contact Number:')),
                ('personnel_branch', models.ForeignKey(verbose_name=' *  Assign branch:', to='Microinsurance_Maintenance.Branch', default='')),
            ],
        ),
        migrations.CreateModel(
            name='PersonnelType',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('personnelTypeName', models.CharField(max_length=50, default='', verbose_name=' *  Personnel Type:')),
            ],
        ),
        migrations.CreateModel(
            name='Underwriter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('underwriter_name', models.CharField(max_length=50, verbose_name=' *  Underwriter name:')),
                ('underwriter_ContactNo', models.CharField(max_length=20, default='', verbose_name=' *  Contact number:')),
                ('underwriter_address', models.TextField(default='', verbose_name=' *  Address:')),
            ],
        ),
        migrations.AddField(
            model_name='personnel',
            name='personnel_ptype',
            field=models.ForeignKey(verbose_name=' *  Personnel type:', to='Microinsurance_Maintenance.PersonnelType', default=''),
        ),
        migrations.AddField(
            model_name='insuranceoffer',
            name='Underwriter_name',
            field=models.ForeignKey(verbose_name=' *  Insurance underwriter:', to='Microinsurance_Maintenance.Underwriter', default=''),
        ),
    ]
