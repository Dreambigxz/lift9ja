from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse
from datetime import date
from django_resized import ResizedImageField
from user.models import PersonalInfomation
from notification import notifications, public_group_notification
from decimal import Decimal
import os

bot_id = '5149735788:AAHF9THgzU7BDTwC6aPckHOsGgaOH1s1ocA'
gc_purchase = 'gspubli'
# group = '-1001740123667,'

from datetime import date, datetime, timedelta
from django.utils import timezone

# Create your models here.

# class Packages(models.Model):
#
#     Plan = [
#         ('standard', 'standard',),
#         ('premium', 'premium',),
#         ('platinum', 'platinum',),
#         ('steel', 'steel',),
#         ('silver', 'silver',),
#         ('gold', 'gold',),
#         ('ruby', 'ruby',),
#         ('diamond', 'diamond',),
#         ('obsidian', 'obsidian',),
#     ]
#
#     plan = models.CharField(max_length=200, default='standard', choices=Plan)
#     amount = models.DecimalField(decimal_places=2, default=0, max_digits=50)
#     daily_earn = models.DecimalField(decimal_places=2, default=0, max_digits=50)
#     total_earn = models.DecimalField(decimal_places=2, default=0, max_digits=50)
#     ref_earning = models.DecimalField(decimal_places=2, default=0, max_digits=50)
#     contract_period = models.CharField(max_length=200, default='4', )
#     date = models.DateTimeField(default=timezone.now)
#
#
#
#     def __str__(self):
#         return self.plan
#
#     class Meta():
#         ordering = ['-date']

class Packages(models.Model):

    Plan = [
            ('0.1GS | ₦2,000', '0.1GS',),
            ('0.2GS  | ₦5,000', '0.2GS',),
            ('0.3GS  | ₦10,000', '0.3GS',),
            ('0.4GS  | ₦15,000', '0.4GS',),
            ('0.5GS  | ₦20,000', '0.5GS',),
            ('0.6GS  | ₦25,000', '0.6GS',),
            ('0.7GS  | ₦30,000', '0.7GS',),
            ('0.8GS  | ₦35,000', '0.8GS',),
            ('0.9GS  | ₦40,000', '0.9GS',),
            ('1GS  | ₦50,000', '1GS',),
            ('2GS  | ₦60,000', '2GS',),
            ('3GS  | ₦100,000', '3GS',),
            ('4GS  | ₦150,000', '4GS',),
            ('5GS  | ₦200,000', '5GS',),
            ('6GS  | ₦300,000', '6GS',),
            ('7GS  | ₦400,000', '7GS',),
            ('8GS  | ₦500,000', '8GS',),
            ('9GS  | ₦750,000', '9GS',),
            ('10GS  | ₦1000,000', '10GS',),
        ]

    plan = models.CharField(max_length=200, default='0.1GS', choices=Plan)
    amount = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    daily_earn = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    total_earn = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    contract_period = models.CharField(max_length=200, default='4', )
    date = models.DateTimeField(default=timezone.now)
    # id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.plan

class UserGold(models.Model):

    type = [
        ('sold', 'sold')

    ]

    Status = [
        ('pending', 'pending'),
        ('active', 'active',),
        ('ended', 'ended',),

    ]

    State = [
        ('awaiting payment', 'awaiting payment'),
        ('awaiting approval', 'awaiting approval'),
        ('approved', 'approved'),
    ]

    ProfitType = [
        ('24', 'Every 24 hrs',),
        ('48', 'Every 48 hrs',),
        ('4days', 'After 4 days'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    plan = models.ForeignKey(Packages, on_delete=models.CASCADE)
    total_earned = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    total_left = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    subscribed_date = models.DateField(default=timezone.now)
    next_run_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, default='pending', choices=Status)
    state = models.CharField(max_length=20, default='awaiting payment', choices=State)
    earn_after = models.CharField(max_length=20, default='Every 24 hrs', choices=ProfitType)
    end_date = models.DateField(default=timezone.now)
    proof = models.ImageField(upload_to='goldstock/userproof/{}'.format(date.today()), null=True, blank=True)
    proof_name = models.CharField(max_length=200, null=True, blank=True)
    filtered = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.proof != None and self.state != 'approved':
            # send notification
            public_group_notification(
                'NEW USER GC PURCHASE PROOF\n\n'
                'View page: {}\n\n'
                'Amount: N{:,}\n'
                'User: {}'.format(
                    'https://goldstockng.herokuapp.com/updateUserGoldStock',
                    Decimal(self.plan.amount),
                    str(self.user.full_name)
                ), bot_id, gc_purchase)

        super(UserGold, self).save()

    def file_name(self):
        file_name = os.path.basename(self.proof.name)
        return file_name

    def __str__(self):
        return self.user.email

    class Meta():
        # ordering = ['-id']
        ordering = ['id']

class Post(models.Model):

    plan = models.ForeignKey(Packages, on_delete=models.CASCADE)
    head_line = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200, default='image')
    images = models.FileField(upload_to='media/post/{}'.format(date.today()), null=True, blank=True)
    video = models.FileField(upload_to='media/post/{}'.format(date.today()), null=True, blank=True)
    content = models.TextField(max_length=3000)
    date = models.DateField(default=timezone.now)
    datetime = models.DateTimeField(default=timezone.now)
    count_activities = models.IntegerField(default=0)
    slug = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.head_line

    class Meta():
        ordering = ['-date']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.head_line)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('localProject:activityDetail', kwargs={
            'slug': self.slug
        })

class Activities(models.Model):

    user = models.CharField(max_length=200, null=True, blank=True)
    profile = models.ForeignKey(PersonalInfomation, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=0)
    comment = models.TextField(max_length=200)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.post)

    class Meta():
        ordering = ['-time']
