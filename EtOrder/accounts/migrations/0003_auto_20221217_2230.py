# Generated by Django 2.2.18 on 2022-12-17 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221217_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='is_staff',
            new_name='is_customer',
        ),
    ]