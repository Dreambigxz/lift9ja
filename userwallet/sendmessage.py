from django.shortcuts import render, redirect
from django.http import request
from django.conf import settings
import json
# import datetime
from django.contrib.sites.shortcuts import get_current_site
import requests
import pytz
utc=pytz.UTC

from django.template import loader
from mailjet_rest import Client
from user.code_generator import code
settings.configure()

# api_key = settings.MAIL_JET_API_KEY_GENERAL_EMAIL
# api_secret = settings.MAIL_JET_API_SECRET_KEY_GENERAL_EMAIL
MAIL_JET_API_KEY = '32d3ccc9673f50deea2fbd0e031f924a'
MAIL_JET_API_SECRET_KEY = '6a1d73ab741ccd1ddbc98c52e8d6f9d4'

api_key = MAIL_JET_API_KEY
api_secret = MAIL_JET_API_SECRET_KEY

mailjet = Client(auth=(api_key, api_secret), version='v3.1')
try:
    from myadmin.models import Administration
    admin = Administration.objects.get(user__is_admin=True)
    COMPANY = admin.site_name
except:
    pass
# Create your views here.

code = code
amount = 5000
email = 'donyemordi@gmaiol.com'

html_message = loader.render_to_string('wallet/charges_mail.html', {
    'name': 'Williams',
    'amount': amount,
    'checkout_id': code,
    'detected': 'https://live.blockcypher.com/btc/tx/{}/'.format('txref'),
    'message': 'Your ${:,} wallet deposit with this code {} detected.'
               ' This means the payment has been detected but it has not yet been validated by the network. When the transaction is fully validated and confirmed by the blockchain network, the payment status changes to Success.'.format(
        amount, code),
    # 'img': '{}/static/temp/images/logo-white.png'.format(get_current_site(request)),
    'sitename': COMPANY,
    'contact_link': '{}/contact-us'.format(get_current_site(request)),
})

data = {
    'Messages': [
        {
            "From": {
                "Email": settings.EMAIL_DELIVERY,
                "Name": COMPANY
            },
            "To": [
                {
                    "Email": email,
                    "Name": ""
                }
            ],
            "Subject": "Payment Detected",
            "HTMLPart": html_message,
            "CustomID": "AppGettingStartedTest"
        }
    ]
}

mailjet.send.create(data=data)