# Generated by Django 5.0 on 2023-12-06 17:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trading', '0003_alter_stock_name_alter_stock_ticker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='name',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='ticker',
        ),
        migrations.AddField(
            model_name='stock',
            name='BOARDID',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='BOARDNAME',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='stock',
            name='CURRENCYID',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='DECIMALS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='FACEUNIT',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='FACEVALUE',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='INSTRID',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='ISIN',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock',
            name='ISSUESIZE',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='LATNAME',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='LISTLEVEL',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='LOTSIZE',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='MARKETCODE',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='MINSTEP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='PREVDATE',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='PREVLEGALCLOSEPRICE',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='PREVPRICE',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='PREVWAPRICE',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='REGNUMBER',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='stock',
            name='REMARKS',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='SECID',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='SECNAME',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='stock',
            name='SECTORID',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='SECTYPE',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='SETTLEDATE',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='SHORTNAME',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='STATUS',
            field=models.CharField(default='', max_length=4),
        ),
    ]
