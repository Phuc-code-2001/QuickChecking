# Generated by Django 3.2.9 on 2021-11-26 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20211126_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_opening',
            field=models.DateField(default=datetime.datetime(2021, 11, 26, 12, 47, 59, 11810)),
        ),
    ]
