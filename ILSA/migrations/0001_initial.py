# Generated by Django 2.0.1 on 2018-01-31 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_uid', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_addr', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('card_uid', models.CharField(max_length=200)),
                ('check_out_time', models.TimeField(verbose_name='Time Checked Out')),
                ('unlockable', models.BooleanField()),
            ],
        ),
    ]
