# Generated by Django 2.2.16 on 2020-12-30 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0031_auto_20201222_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbillinginfo',
            name='billing_address',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userbillinginfo',
            name='billing_city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userbillinginfo',
            name='billing_country_iso2',
            field=models.CharField(default='CL', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userbillinginfo',
            name='billing_district',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userbillinginfo',
            name='id_other',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]
