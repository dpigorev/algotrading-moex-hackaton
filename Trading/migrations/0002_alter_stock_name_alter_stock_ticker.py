# Generated by Django 5.0 on 2023-12-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trading', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.TextField(max_length=10),
        ),
    ]
