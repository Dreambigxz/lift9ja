# Generated by Django 3.2.9 on 2022-01-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userwallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallethistory',
            name='tx_ref',
            field=models.CharField(default=0, max_length=16),
        ),
    ]
