# Generated by Django 4.0.4 on 2022-06-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='customer_code',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='客户编号'),
        ),
    ]
