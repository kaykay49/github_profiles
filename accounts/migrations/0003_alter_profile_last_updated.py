# Generated by Django 3.2.7 on 2021-09-19 12:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210919_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 17, 30, 3, 729865)),
        ),
    ]
