# Generated by Django 4.0.4 on 2022-09-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.IntegerField()),
                ('pen', models.IntegerField()),
                ('notes', models.IntegerField()),
                ('pencil', models.IntegerField()),
                ('paper', models.IntegerField()),
            ],
        ),
    ]