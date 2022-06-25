# Generated by Django 4.0.4 on 2022-06-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_order_customer_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='customer_code',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='客户编号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_code',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='订单编号'),
        ),
    ]
