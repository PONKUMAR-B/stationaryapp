# Generated by Django 4.0.4 on 2022-09-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationaryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='month',
            field=models.CharField(default='', max_length=100),
        ),
    ]
