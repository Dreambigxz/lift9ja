from . import views
from django.urls import path

app_name = 'myadmin'
from . import tg_notifyer
urlpatterns = [
    path('adminControl', views.MyAdmin.as_view()),
    path('updateUserGoldStock', views.UpdatePayment.as_view()),
    path('live-update', views.get_live_update_view, name='live_update'),
    path('pending-payment', views.PendingPayment.as_view(), name='pending-payment'),
    path('process-payment', views.process_payment_view),
    path('add-gs', views.AddGSVIEW.as_view()),
    path('auto-payment', views.auto),
    path('f-data', tg_notifyer.def_fake_data),

    # path('gs-daily-payment', views.gs_daily_payment_view),
    # path('statistics', views.statistics),

    # http://127.0.0.1:8000/gs-daily-payment?run=2
    # goldstockng.com/gs-daily-payment?run=2

]