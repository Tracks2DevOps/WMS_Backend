# Generated by Django 4.1.5 on 2023-01-05 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_alter_warehouseorders_date_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseorders',
            name='date_received',
            field=models.DateField(default=datetime.datetime(2023, 1, 5, 0, 0), verbose_name='Date Received by Warehouse'),
        ),
    ]