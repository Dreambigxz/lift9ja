# Generated by Django 3.2.9 on 2022-02-10 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20220208_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergold',
            name='filtered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usergold',
            name='proof_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='media/post/2022-02-10'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/post/2022-02-10'),
        ),
        migrations.AlterField(
            model_name='usergold',
            name='proof',
            field=models.ImageField(blank=True, null=True, upload_to='goldstock/userproof/2022-02-10'),
        ),
    ]