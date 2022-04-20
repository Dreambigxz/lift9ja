import uuid
import requests
import json
from base64 import b64encode
from django.conf import settings
from transaction_id import get_transaction_id
from myadmin.models import *
COMPANY = 'GOLD STOCK'
mac_id = (uuid.uuid4().hex[:12])

try:

    admin = Administration.objects.get(user__top_admin=True)

    if admin.flutter_wave == 'nexzus':
        FLUTTER_WAVE_SECRET_KEY = settings.FLUTTER_WAVE_SECRET_KEY2
    else:
        FLUTTER_WAVE_SECRET_KEY = settings.FLUTTER_WAVE_SECRET_KEY

except:
    admin = ''

def deposit_api(tx_ref, amount, user_id, email, name, currency, current_site):

    url = 'https://api.flutterwave.com/v3/payments'
    headers = {
        'content-type': 'application/json',
        'Authorization': settings.FLUTTER_WAVE_SECRET_KEY
    }

    data = {
        "tx_ref": tx_ref,
        "amount": amount,
        "currency": currency,
        # "redirect_url": '/process-deposit',
        "redirect_url": 'https://alertifyng.com/process-deposit',
        "payment_options": "card",
        "meta": {
            "consumer_id": user_id,
            "consumer_mac": mac_id,
        },
        "customer": {
            "email": email,
            "name": name
        },
        "customizations": {
            "title": "My Wallet Deposit",
            "description": "I {} is depositing the sum of {} to my peek wallet".format(name, amount),
            "logo": "https://alertifyng.com/static/assets/images/icons/favicon.jpeg"
        }
    }

    r = requests.post(url, headers=headers, json=data)

    data = (r.content)
    data_decode = data.decode('utf8')
    cvt_to_dict = json.loads(data_decode)
    print('this is ', cvt_to_dict)
    link = (cvt_to_dict['data']['link'])
    return link

def verify_transanction(transaction_id):

    url = 'https://api.flutterwave.com/v3/transactions/{}/verify'.format(transaction_id)
    headers = {
        'content-type': 'application/json',
        'Authorization': settings.FLUTTER_WAVE_SECRET_KEY
    }

    r = requests.get(url=url, headers=headers)

    get_data = r.content
    # print('this a status data', get_data)
    decode_data = get_data.decode('utf8')
    get_as_json = json.loads(decode_data)
    return  get_as_json

def verify_account(account_number, account_bank):
    url = 'https://api.ravepay.co/flwv3-pug/getpaidx/api/resolve_account'

    headers = {
        'content-type': 'application/json',
        'Authorization': settings.FLUTTER_WAVE_SECRET_KEY
    }

    data = {

        "recipientaccount": account_number,
        "destbankcode": account_bank,
        'PBFPubKey': settings.FLUTTER_WAVE_PUB_KEY
    }

    r = requests.post(url, headers=headers, json=data)

    print(r)
    data = (r.content)

    data_decode = data.decode('utf8')
    cvt_to_dict = json.loads(data_decode)
    return cvt_to_dict

def withdraw(account_bank, account_number, amount, user, mac_id):


    if admin.flutter_wave == 'nexzus':
        FLUTTER_WAVE_SECRET_KEY = settings.FLUTTER_WAVE_SECRET_KEY2
    else:
        FLUTTER_WAVE_SECRET_KEY = settings.FLUTTER_WAVE_SECRET_KEY

    url = 'https://api.flutterwave.com/v3/transfers'


    headers = {
        'content-type': 'application/json',
        'Authorization': FLUTTER_WAVE_SECRET_KEY
    }

    data = {

    "account_bank": account_bank,
    "account_number": account_number,
    "amount": amount,
    "narration": "{} Payment to {}".format(COMPANY, user.capitalize()),
    "currency": "NGN",
    "reference": mac_id,
    "callback_url": "https://{}/transfer_response/".format(settings.ALLOWED_HOSTS[0]),
    "debit_currency": "NGN"
    }

    r = requests.post(url, headers=headers, json=data)

    data = (r.content)
    data_decode = data.decode('utf8')
    cvt_to_dict = json.loads(data_decode)
    print(cvt_to_dict)
    return cvt_to_dict

def flutter_top_up(amount, number,):

    url = 'https://api.flutterwave.com/v3/bills'

    headers = {
        'content-type': 'application/json',
        'Authorization': settings.FLUTTER_WAVE_SECRET_KEY
    }


    data = {
       "country": "NG",
       "customer": number,
       "amount": amount,
       "recurrence": "ONCE",
       "type": "AIRTIME",
       "reference": get_transaction_id()
    }

    r = requests.post(url, headers=headers, json=data)

    data = (r.content)
    data_decode = data.decode('utf8')
    cvt_to_dict = json.loads(data_decode)
    return cvt_to_dict

def transfer_deposit(tx_ref, amount, email, currency):

    print('this is amount', amount)

    url = 'https://api.flutterwave.com/v3/charges?type=bank_transfer'
    headers = {
        'content-type': 'application/json',
        'Authorization': settings.FLUTTER_WAVE_SECRET_KEY
    }

    data = {
        "tx_ref": tx_ref,
        "amount": amount,
        "currency": currency,
        "email": email,
        "duration": 2,
        "frequency": 5,
        "narration": "your digital wallet, no charges apply",
        "is_permanent": False

        }

    r = requests.post(url, headers=headers, json=data)

    data = (r.content)

    print(data)
    data_decode = data.decode('utf8')
    cvt_to_dict = json.loads(data_decode)

    data = (cvt_to_dict)
    return data

def static_bank_transfer():

    url = 'https://api.ravepay.co/flwv3-pug/getpaidx/api/charge'

    headers = {
        'content-type': 'application/json',
        'Authorization': settings.FLUTTER_WAVE_SECRET_KEY
    }

    data = {
            "amount": 100,
            "PBFPubKey":  settings.FLUTTER_WAVE_PUB_KEY,
            "currency": "NGN",
            "country": "NG",
            "email": "user@example.com",
            "txRef": "bank-transfer-1561058350398",
            "meta": [{"metaname": "test", "metavalue": "12383"}],
            "payment_type": "banktransfer",
            "ip": "123.0.1.3",
            "is_bank_transfer": True,
            "firstname": "Flutterwave",
            "lastname": "Tester"
        }



    r = requests.post(url, headers=headers, json=data)

    data = (r.content)

    print(data)
    # data_decode = data.decode('utf8')
    # cvt_to_dict = json.loads(data_decode)
    #
    # data = (cvt_to_dict)
    # return data
