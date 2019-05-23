# Generated by Django 2.1.3 on 2018-11-11 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacathon', '0010_auto_20181111_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 11, 11, 6, 21, 38, 632684)),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.CharField(choices=[('tel', 'Tel'), ('card', 'Card'), ('bug', 'Bug'), ('evaluate', 'Evaluate'), ('feedback', 'Feedback'), ('question', 'Question'), ('transaction', 'Transaction'), ('recommend', 'Recommend')], max_length=1000),
        ),
    ]
