from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from token_generator import account_number_generator
from django.utils import timezone
from user.models import MyUser
from django.utils.text import slugify
# Create your models here.

# Create your models here.
class Administration(models.Model):

    FLUTTER_WAVE_ACCOUNTS = [
        ('others', 'others',),
        ('nexzus', 'nexzus',)
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    total_deposit = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    total_withdraw = models.DecimalField(decimal_places=2, default=0, max_digits=50)

    tot_users = models.IntegerField(default=200)
    avg_traders = models.IntegerField(default=400)
    total_transaction = models.DecimalField(decimal_places=2, default=7000, max_digits=50)

    # bill_settlement_fake = models.DecimalField(decimal_places=2, default=7000, max_digits=50)
    bill_settlement = models.DecimalField(decimal_places=2, default=7000, max_digits=50)
    total_traded = models.DecimalField(decimal_places=2, default=7000, max_digits=50)
    total_trade_return = models.DecimalField(decimal_places=2, default=7000, max_digits=50)

    total_sent_to_flutter_wave = models.DecimalField(decimal_places=2, default=7000, max_digits=50)
    total_available_balance = models.DecimalField(decimal_places=2, default=7000, max_digits=50)

    site_name = models.CharField(max_length=200, default='Doughscoin Limited')
    site_url = models.CharField(max_length=200, default='doughscoin.com')
    phone_number = models.CharField(max_length=200, default='+1 (610) 215‑9003')
    email = models.CharField(max_length=200, default='support@doughscoin.com')

    data_gifting = models.BooleanField(default=True)

    live_bot = models.BooleanField(default=True)
    site_available = models.BooleanField(default=True)
    available_message = models.TextField(default='Your registrations in GS is Successful,\n\n'
                                                                 'kindly login to your account and purchase SG gold of your choice')
    not_available_message = models.TextField(default='Your registrations in GS is Successful.\n\n'
                                                                     'Market currently closed, please come back 9am')
    market_message = models.CharField(max_length=200, default='Market currently closed, please come back 9am')
    flutter_wave = models.CharField(max_length=20, default='others', choices=FLUTTER_WAVE_ACCOUNTS)


    def __str__(self):
        return self.user.username

class AdminBank(models.Model):
    bank_name = models.CharField(max_length=200, default='Kuda Micro Finance Bank')
    account_number = models.CharField(max_length=20, default='2003094297')
    account_name = models.CharField(max_length=200, default='Olufemi Ilori')

    def __str__(self):
        return self.bank_name

class AdminMessage(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    mess = models.TextField(blank=True, null=True)
    first_save = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.mess

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.first_save == True:
            users = MyUser.objects.filter(read_message=True)
            print(users.count())
            for i in users:
                print(i)
                i.read_message = False
                i.save()
        self.first_save = False
        super(AdminMessage, self).save()

