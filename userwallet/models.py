from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from token_generator import account_number_generator
from django.utils import timezone
from django.utils.text import slugify
from user.models import PersonalInfomation, UserPreference
# Create your models here.

"""
devote acoustic drum

major black expect

rude orbit large

delay inflict price
"""
class UserWallet(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    user_balance = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    user_account_number = models.FloatField(default=0000)
    get_first_deposit = models.BooleanField(null=True, blank=True, default=False)
    testified = models.BooleanField(null=True, blank=True, default=False)
    to_cash_out = models.BooleanField(null=True, blank=True, default=False)



    def __str__(self):
        return self.user.email

    class Meta:
        permissions = (
            ('read_item', 'Can read item'),
        )

class WithdrawPin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
    pin = models.CharField(max_length=200, default='0000')

    def __str__(self):
        return self.user.email

class WalletHistory(models.Model):

    TRANSACTION_STATUS=[
        ('success', 'success',),
        ('pending', 'pending',),
        ('failed', 'failed',),
    ]

    Transaction_type = [
        ('withdraw', 'withdraw',),
        ('deposit', 'deposit',),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    wallet = models.ForeignKey(UserWallet, on_delete=models.CASCADE, null=True, blank=True)
    transaction_id = models.CharField(max_length=20, default=0)
    tx_ref = models.CharField(max_length=16, default=0)
    type = models.CharField(max_length=200, null=True, choices=Transaction_type)
    amount = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(default='pending', choices=TRANSACTION_STATUS, max_length=12)

    account_number = models.CharField(null=True, blank=True, max_length=200)
    bank_name = models.CharField(null=True, blank=True, max_length=200)
    beneficiary = models.CharField(null=True, blank=True, max_length=200)
    bank_code = models.CharField(null=True, blank=True, max_length=200)
    stamp_charge = models.DecimalField(decimal_places=2, default=0, max_digits=50)


    def __str__(self):
        return self.user.email


    class Meta():
        ordering = ['-date']

    # def save(self, *args, **kwargs):
    #
    #     self.slug = slugify(str(self.code)+self.user.username)
    #     self.code = self.code.lower()
    #     super(WalletHistory, self).save_base(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #
    #     return reverse('wallet:depositDetailHistory', kwargs={
    #         'slug': self.slug
    #     })


class WithdrawReview(models.Model):


    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    wallet = models.ForeignKey(UserWallet, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.CharField(max_length=200, default=0)
    account_number = models.CharField(max_length=200, default=0)
    beneficiary = models.CharField(max_length=200, default=0)
    bank_name = models.CharField(max_length=200, default=0)
    bank_code = models.CharField(max_length=200, default=0)
    time_updated = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.user.email

    class Meta():
        ordering = ['-time_updated']


class TotalFundingToday(models.Model):
    amount = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    datetime = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.amount)



# class BankTransfer(models.Model):
#
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
#     account_name = models.CharField(max_length=200)
#     account_number = models.CharField(max_length=200)
#     bank = models.CharField(max_length=200)
#     amount = models.DecimalField(decimal_places=2, default=0, max_digits=50)
#
#     def __str__(self):
#         return str(self.user.email)
