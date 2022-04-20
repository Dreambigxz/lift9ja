from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class UserReferral(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='referral', on_delete=models.CASCADE, null=True, blank=True)
    referred = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    earn = models.DecimalField(decimal_places=2, default=0, max_digits=50)
    active = models.BooleanField(default=False)
    withdrawn = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=timezone.now)
    withdrawn_date = models.DateTimeField(null=True, blank=True, default=None)



    def __str__(self):
        return self.user.email


