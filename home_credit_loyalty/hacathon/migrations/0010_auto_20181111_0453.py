# Generated by Django 2.1.3 on 2018-11-10 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacathon', '0009_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 11, 11, 4, 53, 48, 463248)),
        ),
    ]
