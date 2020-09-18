# Generated by Django 3.1.1 on 2020-09-17 19:07

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapische', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coordinates',
            options={'verbose_name': 'Координаты', 'verbose_name_plural': 'Координаты'},
        ),
        migrations.RemoveField(
            model_name='coordinates',
            name='date',
        ),
        migrations.AlterField(
            model_name='coordinates',
            name='pointer',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, srid=4326),
        ),
    ]