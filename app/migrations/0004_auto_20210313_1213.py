# Generated by Django 3.0.2 on 2021-03-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210313_0628'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='nickname',
            field=models.TextField(default='Нету'),
        ),
        migrations.AlterField(
            model_name='account',
            name='reg_date',
            field=models.TextField(default='2021.03.13 15:13'),
        ),
    ]
