# Generated by Django 2.2.4 on 2019-08-15 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_auto_20190815_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='bike_id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart_id',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
