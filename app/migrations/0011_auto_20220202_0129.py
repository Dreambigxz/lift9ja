# Generated by Django 3.2.9 on 2022-02-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220202_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='packages',
            name='contract_period',
            field=models.CharField(default='4', max_length=200),
        ),
        migrations.AlterField(
            model_name='packages',
            name='plan',
            field=models.CharField(choices=[('0.1GS | ₦2,000', '2000'), ('0.2GS  | ₦5,000', '5000'), ('0.3GS  | ₦10,000', '10000'), ('0.4GS  | ₦15,000', '15000'), ('0.5GS  | ₦20,000', '20000'), ('0.6GS  | ₦25,000', '25000'), ('0.7GS  | ₦30,000', '30000'), ('0.8GS  | ₦35,000', '35000'), ('0.9GS  | ₦40,000', '40000'), ('1GS  | ₦50,000', '50000'), ('2GS  | ₦60,000', '60000'), ('3GS  | ₦100,000', '100000'), ('4GS  | ₦150,000', '150000'), ('5GS  | ₦200,000', '200000'), ('6GS  | ₦300,000', '300000'), ('7GS  | ₦400,000', '400000'), ('8GS  | ₦500,000', '500000'), ('9GS  | ₦750,000', '750000'), ('10GS  | ₦1000,000', '1000000')], default='0.1GS', max_length=200),
        ),
        migrations.AlterField(
            model_name='usergold',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('active', 'active'), ('ended', 'ended')], default='pending', max_length=20),
        ),
    ]
