# Generated by Django 2.2.18 on 2022-12-17 16:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='branch',
            new_name='customer_type',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='subject',
            new_name='Staff_subject',
        ),
        migrations.AddField(
            model_name='customer',
            name='ip_location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, dim=3, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
