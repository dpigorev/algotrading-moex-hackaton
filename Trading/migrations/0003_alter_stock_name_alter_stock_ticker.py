# Generated by Django 5.0 on 2023-12-05 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trading', '0002_alter_stock_name_alter_stock_ticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(max_length=10),
        ),
    ]