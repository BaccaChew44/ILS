# Generated by Django 2.0.1 on 2018-02-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ILSA', '0005_auto_20180202_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='card_uid',
            field=models.CharField(default='0', max_length=200),
        ),
        migrations.AlterField(
            model_name='locker',
            name='check_out_time',
            field=models.TimeField(default='14:44:30', verbose_name='Time Last Used'),
        ),
    ]