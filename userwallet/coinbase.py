import requests
import json
import uuid
from django.conf import settings
mac_id = (uuid.uuid4().hex[:12])
from base64 import b64encode
from transaction_id import get_transaction_id

from coinbase_commerce.client import Client
client = Client(api_key=settings.COINBASE_SECRET_KEY)

def coinbase_deposit_api(amount, currency, name, email):

    checkout_info = {

        "name": 'E-wallet Account Deposit For {}'.format(name.title()),
        "description": email,
        "pricing_type": 'fixed_price',
        "local_price": {
            "amount": amount,
            "currency": currency
        },
        "requested_info": [ ]
    }

    checkout = client.charge.create(**checkout_info)

    return checkout





    # r = requests.post(url, headers=headers, json=data)
    #
    # data = (r.content)
    # data_decode = data.decode('utf8')
    # cvt_to_dict = json.loads(data_decode)
    # print('this is ', cvt_to_dict)
    # link = (cvt_to_dict['data']['link'])
    # return link
