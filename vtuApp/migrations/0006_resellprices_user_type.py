# Generated by Django 3.2.9 on 2022-01-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtuApp', '0005_resellprices'),
    ]

    operations = [
        migrations.AddField(
            model_name='resellprices',
            name='user_type',
            field=models.CharField(choices=[('admin', 'admin'), ('agent', 'agent'), ('end_user', 'end_user')], default='end_user', max_length=12),
        ),
    ]