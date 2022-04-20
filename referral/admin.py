from django.contrib import admin
from .models import UserReferral
# Register your models here.
class Referral(admin.ModelAdmin):

    list_display = ('user', 'referred', 'earn', 'active', 'join_date', 'withdrawn_date', 'withdrawn')
    search_fields = ['user__email', 'referred__full_name', 'referred__email']


admin.site.register(UserReferral, Referral)
