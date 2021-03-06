# Generated by Django 3.1.2 on 2020-10-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='value_baseline',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='value_stdev',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
