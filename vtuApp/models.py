from django.db import models
from django.conf import settings
from django.utils import timezone
from gb_calculator import *

# Create your models here.

class MyContacts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    contact = models.CharField(null=True, blank=True, max_length=11)

    def __str__(self):
        return str(self.contact)

class TopUpHistory(models.Model):
    TRANSACTION_STATUS = [
        ('success', 'success',),
        ('pending', 'pending',),
        ('failed', 'failed',),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    network = models.CharField(max_length=20, null=True)
    amount = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    plan = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, choices=TRANSACTION_STATUS, default='pending')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user.email)

    class Meta():
        ordering = ['-date']

class UserType(models.Model):

    USER_TYPE = (
        ('admin', 'admin'),
        ('agent', 'agent'),
        ('end_user', 'end_user')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.CharField(max_length=12, default='end_user', choices=USER_TYPE)
    percent = models.IntegerField(default=25)
    gifted = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.email)

class CgWallet(models.Model):

    Network = [
        ('12', 'mtn',),
        ('9', '9mobile',),
        ('8', 'airtel',),
        ('7', 'glo',),
    ]

    data_balance = models.FloatField(max_length=200, null=True, blank=True)
    network = models.CharField(max_length=200, null=True, blank=True, choices=Network)
    val = models.CharField(max_length=200, null=True, blank=True, default='MB')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.network

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print(conv_MB_to_GB(self.data_balance))
        if conv_MB_to_GB(self.data_balance) < conv_MB_to_GB(900):
            self.active = False
        elif conv_MB_to_GB(self.data_balance) >= conv_MB_to_GB(1000):
            self.val = 'GB'
            self.active = True
        else:
            self.val = 'MB'
        super(CgWallet, self).save()
