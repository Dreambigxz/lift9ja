# Generated by Django 3.2.9 on 2022-02-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_packages_total_earn'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergold',
            name='proof',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='usergold',
            name='status',
            field=models.CharField(choices=[('awaiting payment', 'awaiting payment'), ('pending', 'pending'), ('active', 'active'), ('ended', 'ended')], default='awaiting payment', max_length=20),
        ),
    ]
