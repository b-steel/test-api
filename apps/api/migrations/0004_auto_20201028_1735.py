# Generated by Django 3.1.2 on 2020-10-28 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201028_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solarproject',
            name='parent',
        ),
        migrations.DeleteModel(
            name='SolarData',
        ),
    ]
