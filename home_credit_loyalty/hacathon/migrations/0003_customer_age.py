# Generated by Django 2.1.3 on 2018-11-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacathon', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
