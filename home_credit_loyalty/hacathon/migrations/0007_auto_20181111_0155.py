# Generated by Django 2.1.3 on 2018-11-10 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacathon', '0006_auto_20181111_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='expiredDate',
            new_name='type',
        ),
    ]
