import requests
import json
import uuid
from django.conf import settings
mac_id = (uuid.uuid4().hex[:12])
from base64 import b64encode
from coins.transaction_id import get_transaction_id

# def pay_crpto(amount, track_id, nonce):
#
#
#     # data = {
#     #     "track_id": track_id,
#     #     "amount": amount,
#     #     "nonce": nonce,
#     #
#     # }
#
#     link = requests.get('https://paxful.com/wallet/pay?'
#                         'merchant={}&'
#                         'apikey={}&'
#                         'apiseal={}&'
#                         'nonce={}&'
#                         'to={}&'
#                         'track_id={}&'
#                         'amount={}'.format('WDZkGoR7k7M',
#                                            'fHvheMDyu1y1jaJwQIXFcV1Qzc9k30nx',
#                                            1234,nonce,)
#                         )
#
#     return link
