# Generated by Django 2.2.4 on 2019-08-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20190815_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
