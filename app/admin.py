from django.contrib import admin
from .models import *


class ListAdmin(admin.ModelAdmin):
    list_display = ('plan', 'daily_earn', 'total_earn',)

    search_fields = ['plan']

class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'state',
                    'earn_after', 'total_earned',
                    'total_left', 'subscribed_date',
                    'next_run_date',
                    'end_date', 'proof_name')

    search_fields = ['user__email', 'user__full_name', 'user__username', 'status', 'state', 'proof_name']


admin.site.register(Packages, ListAdmin)
admin.site.register(UserGold, SubscribersAdmin)
# admin.site.register(Post)
# admin.site.register(Activities)