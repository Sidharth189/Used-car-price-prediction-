# Generated by Django 4.1.7 on 2023-03-16 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceprediction', '0005_alter_car_p_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='p_price',
        ),
        migrations.AddField(
            model_name='car',
            name='present_price',
            field=models.FloatField(default='NULL'),
        ),
    ]
