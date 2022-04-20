from django.db import models
import random
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.template.defaultfilters import slugify
import datetime
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.core.exceptions import ValidationError
from django_resized import ResizedImageField
# Create your models here.



class MyUserManager(BaseUserManager):
    def create_user(self,  email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address or User Name')

        if not username:

            raise  ValidationError('Username exist')

        user = self.model(
            email=self.normalize_email(email),
            username=  username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(

            username= username,
            email= email,
            password=password,
        )


        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):

    username = models.CharField(verbose_name='User Name',
                                unique=True,
                                max_length=100,)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    full_name = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    top_admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    reset_password = models.BooleanField(default=False)
    otp = models.CharField(max_length=7, default=000)
    mail = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    read_message = models.BooleanField(default=False)
    count_login = models.IntegerField(default=0)
    gender = models.CharField(max_length=5, default='👨🏾‍💻')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' ]

    def __str__(self):
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class PersonalInfomation(models.Model):

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    phone_number = models.CharField(default=234, max_length=20, null=True, blank=True)
    user_image = ResizedImageField(size=[100, 100], upload_to='images/profile', null=True, blank=True)
    date_of_bith = models.DateField(null=True, blank=True)
    user_address = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    country_code = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    image = models.BooleanField(default=False)


    def __str__(self):
        return self.user.email

    def user_img_url(self):
        try:
            url= self.user_image.url
        except:
            url = ''

        return url

class UserPreference(models.Model):

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    two_factor_auth = models.BooleanField(default=True)
    ref_link = models.CharField(max_length=200, null=True)
    ip = models.CharField(max_length=200, null=True,)
    location = models.CharField(max_length=200, null=True,)

    def __str__(self):
        return self.user.email

class TESTIMONIA(models.Model):

    username = models.CharField(max_length=200, default='none')
    personal_info = models.ForeignKey(PersonalInfomation, on_delete=models.CASCADE, null=True, blank=True)
    testify = models.TextField(null=True)
    active = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return  self.username

    class Meta():
        ordering = ['-time']

class ContactUs(models.Model):

    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200)
    telegram_username = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    pending = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.email

#export PATH=$PATH:/snap/bin
