# Generated by Django 2.1.3 on 2018-11-10 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacathon', '0004_auto_20181110_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]