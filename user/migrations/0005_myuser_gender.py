# Generated by Django 4.0.3 on 2022-04-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_myuser_read_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(default='👨🏾\u200d💻', max_length=5),
        ),
    ]
