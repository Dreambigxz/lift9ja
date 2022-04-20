from . import views
from django.urls import path
app_name = 'wallet'

urlpatterns = [

    path('buy-coupon', views.UserDeposit.as_view(), name='deposit'),
    path('update-coupon', views.UpdateCouponCode.as_view()),
    path('process-deposit', views.process_deposit,),
    path('mywebhook', views.deposit_webhook, name='webhookView'),

    path('process-withdraw', views.process_withdraw, name='processW'),
    path('withdraw', views.UserWalletWithdrawal.as_view(), name='walletWithdraw'),
    path('pin', views.ChangePin.as_view(), name='changePin'),


]