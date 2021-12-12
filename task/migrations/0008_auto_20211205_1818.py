# Generated by Django 3.2.9 on 2021-12-05 11:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='time_checked',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 18, 18, 3, 808193)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_of_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 5, 11, 18, 3, 808193, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_opening',
            field=models.DateField(default=datetime.datetime(2021, 12, 5, 11, 18, 3, 808193, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_time',
            field=models.TimeField(default=datetime.time(11, 18, 3, 808193)),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.TimeField(default=datetime.time(11, 18, 3, 808193)),
        ),
    ]