# Generated by Django 3.1.2 on 2020-10-13 12:58

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
