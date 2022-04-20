from . import views
from django.urls import path

app_name = 'localProject'

urlpatterns = [

    path('', views.HomeView.as_view(), name='Home'),
    path('dashboard', views.Welcome.as_view(), name='welcome'),
    path('about-us', views.AboutUs.as_view(), name='about'),
    path('privacy-policy', views.PrivacyPolicy.as_view(), name='privacy'),
    path('contact-us', views.Contact.as_view(), name='contact'),
    path('faq', views.Faq.as_view(), name='faq'),

    ###########################################################

    path('buy-gold', views.PlanSubscription.as_view()),
    path('my-gs-data', views.MyOffice.as_view()),
    path('upload-proof', views.upload_proof),
    # path('sell-share', views.SellShare.as_view()),

    path('messages', views.MessagesView.as_view()),

]
