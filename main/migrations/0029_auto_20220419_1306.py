# Generated by Django 3.2.10 on 2022-04-19 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20220419_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='payment_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='bills',
            name='status',
            field=models.CharField(blank=True, choices=[('y', 'Paid'), ('n', 'Pending')], max_length=1),
        ),
        migrations.AlterField(
            model_name='notice',
            name='showtill',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 20, 13, 6, 8, 101741)),
        ),
    ]