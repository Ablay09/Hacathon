# Generated by Django 2.1.3 on 2018-11-10 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hacathon', '0003_customer_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hacathon.Customer'),
        ),
        migrations.AlterField(
            model_name='task',
            name='expiredDate',
            field=models.CharField(choices=[('tel', 'Tel'), ('card', 'Card'), ('bug', 'Bug'), ('evaluate', 'Evaluate'), ('feedback', 'Feedback'), ('question', 'Question'), ('transaction', 'Transaction')], max_length=1000),
        ),
    ]