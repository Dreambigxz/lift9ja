# Generated by Django 3.2.9 on 2022-02-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220202_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='plan',
            field=models.CharField(choices=[('0.1GS | ₦2,000', '0.1GS'), ('0.2GS  | ₦5,000', '0.2GS'), ('0.3GS  | ₦10,000', '0.3GS'), ('0.4GS  | ₦15,000', '0.4GS'), ('0.5GS  | ₦20,000', '0.5GS'), ('0.6GS  | ₦25,000', '0.6GS'), ('0.7GS  | ₦30,000', '0.7GS'), ('0.8GS  | ₦35,000', '0.8GS'), ('0.9GS  | ₦40,000', '0.9GS'), ('1GS  | ₦50,000', '1GS'), ('2GS  | ₦60,000', '2GS'), ('3GS  | ₦100,000', '3GS'), ('4GS  | ₦150,000', '4GS'), ('5GS  | ₦200,000', '5GS'), ('6GS  | ₦300,000', '6GS'), ('7GS  | ₦400,000', '7GS'), ('8GS  | ₦500,000', '8GS'), ('9GS  | ₦750,000', '9GS'), ('10GS  | ₦1000,000', '10GS')], default='0.1GS', max_length=200),
        ),
        migrations.AlterField(
            model_name='packages',
            name='total_earn',
            field=models.FloatField(default=0),
        ),
    ]
