from . import views
from django.urls import path

app_name = 'referral'

urlpatterns = [

    path('my-referral', views.MyReferral.as_view(), name='myRef'),
    path('withdraw-referral', views.withdraw_ref, name='withdrawMyRef'),

]