# Generated by Django 3.2.10 on 2022-04-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20220405_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
