# Generated by Django 5.0 on 2023-12-07 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trading', '0004_remove_stock_name_remove_stock_ticker_stock_boardid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='PREVDATE',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 7, 20, 52, 29, 377074)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='SETTLEDATE',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 7, 20, 52, 29, 377278)),
        ),
    ]