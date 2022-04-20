from django.contrib import admin
from .models import UserWallet, WalletHistory, WithdrawPin, TotalFundingToday, WithdrawReview


class ListAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_balance', 'user_account_number')

    search_fields = ['user__email']


class WalletHistoryList(admin.ModelAdmin):
    list_display = ('user', 'tx_ref', 'type', 'amount', 'status', 'date')

    search_fields = ['account_number', 'user__email', 'user__full_name', 'tx_ref', 'amount']

class Pin(admin.ModelAdmin):
    list_display = ('user', 'pin')

    search_fields = ['user__email']

class TotalDailyfunding(admin.ModelAdmin):
    list_display = ('amount', 'datetime' )


# Register your models here.
admin.site.register(UserWallet, ListAdmin)
admin.site.register(WalletHistory, WalletHistoryList)
admin.site.register(WithdrawPin, Pin)
# admin.site.register(TotalFundingToday, TotalDailyfunding)
admin.site.register(WithdrawReview)
