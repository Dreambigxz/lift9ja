# Generated by Django 3.2.9 on 2022-02-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220202_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='total_earn',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]