# Generated by Django 4.0.4 on 2022-06-23 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_supply_item_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sc',
        ),
    ]
