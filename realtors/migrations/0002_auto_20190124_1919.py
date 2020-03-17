# Generated by Django 2.1.4 on 2019-01-24 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 1, 24, 19, 19, 34, 420250)),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='is_mvp',
            field=models.BooleanField(default=False),
        ),
    ]
