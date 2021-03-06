# Generated by Django 3.2.9 on 2022-02-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220123_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='plan',
            field=models.CharField(choices=[('5000', '5000'), ('10000', '10000'), ('15000', '15000'), ('20000', '20000'), ('30000', '30000'), ('40000', '45000'), ('50000', '50000'), ('100000', '100000'), ('200000', '200000'), ('300000', '300000'), ('400000', '400000'), ('500000', '500000')], default='5000', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='media/post/2022-02-01'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/post/2022-02-01'),
        ),
    ]
