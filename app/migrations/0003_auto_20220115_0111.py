# Generated by Django 3.2.9 on 2022-01-15 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20220114_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_earned', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('total_left', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('subscribed_date', models.DateField(default=django.utils.timezone.now)),
                ('next_run_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('bought', 'bought'), ('active', 'active'), ('ended', 'ended')], default='active', max_length=20)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-next_run_date'],
            },
        ),
        migrations.AlterField(
            model_name='packages',
            name='plan',
            field=models.CharField(choices=[('5000', '5000'), ('10000', '10000'), ('15000', '15000'), ('20000', '20000'), ('25000', '25000'), ('30000', '30000'), ('45000', '45000'), ('50000', '5000'), ('100000', '100000'), ('200000', '200000'), ('300000', '300000'), ('400000', '400000'), ('500000', '500000')], default='5000', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='media/post/2022-01-15'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/post/2022-01-15'),
        ),
        migrations.DeleteModel(
            name='Subscibers',
        ),
        migrations.AddField(
            model_name='shares',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.packages'),
        ),
        migrations.AddField(
            model_name='shares',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
