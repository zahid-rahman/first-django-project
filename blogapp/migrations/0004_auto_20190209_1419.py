# Generated by Django 2.1.5 on 2019-02-09 14:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20190209_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 9, 14, 19, 5, 317152, tzinfo=utc)),
        ),
    ]