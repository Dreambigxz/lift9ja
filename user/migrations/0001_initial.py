# Generated by Django 3.2.6 on 2021-12-09 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='User Name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('reset_password', models.BooleanField(default=False)),
                ('otp', models.CharField(default=0, max_length=7)),
                ('mail', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('telegram_username', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField()),
                ('pending', models.BooleanField(default=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfomation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default=234, max_length=20, null=True)),
                ('user_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[100, 100], upload_to='images/profile')),
                ('date_of_bith', models.DateField(blank=True, null=True)),
                ('user_address', models.CharField(blank=True, max_length=60, null=True)),
                ('state', models.CharField(blank=True, max_length=60, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('country_code', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('two_factor_auth', models.BooleanField(default=True)),
                ('ref_link', models.CharField(max_length=200, null=True)),
                ('ip', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TESTIMONIA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='none', max_length=200)),
                ('testify', models.TextField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('personal_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.personalinfomation')),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]