from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [

    path('login', views.Login.as_view()),
    path('register', views.Register.as_view()),

    path('logout', views.Logout.as_view(), name='logout'),
    path('emailVerification/<uidb64>/<token>', views.activate, name='emailActivate'),
    path('resendemailVerification/<email>', views.resend_verification, name='resendemailActivate'),
    path('forgot-password', views.LostPassword.as_view(), name='forgot_password'),
    path('reset-password', views.ResetPassword.as_view(), name='resetPassword'),

    path('saveiplocation', views.location_ip, name='user_ip_location'),
    path('my-account', views.Account.as_view(), name='account'),
    path('testify', views.TestimoniaView.as_view(), name='testify'),
]