# Generated by Django 2.1.4 on 2019-01-24 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20190124_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 1, 24, 19, 50, 3, 143798)),
        ),
    ]
