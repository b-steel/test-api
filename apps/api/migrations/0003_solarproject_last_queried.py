# Generated by Django 3.1.4 on 2020-12-11 05:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201030_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='solarproject',
            name='last_queried',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last queried'),
            preserve_default=False,
        ),
    ]
