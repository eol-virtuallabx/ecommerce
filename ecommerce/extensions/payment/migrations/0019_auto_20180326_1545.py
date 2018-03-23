# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-26 15:45
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0018_create_stripe_switch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdncheckfailure',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='sdncheckfailure',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
