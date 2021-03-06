# Generated by Django 3.2.9 on 2022-02-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_usergold_proof_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='media/post/2022-02-11'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/post/2022-02-11'),
        ),
        migrations.AlterField(
            model_name='usergold',
            name='proof',
            field=models.ImageField(blank=True, null=True, upload_to='goldstock/userproof/2022-02-11'),
        ),
    ]
