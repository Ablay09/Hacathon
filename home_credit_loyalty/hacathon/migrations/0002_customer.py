# Generated by Django 2.1.3 on 2018-11-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacathon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('tasks', models.ManyToManyField(blank=True, null=True, related_name='tasks', to='hacathon.Task')),
            ],
        ),
    ]