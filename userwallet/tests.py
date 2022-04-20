import datetime
import requests
import requests as req
from datetime import date, datetime
# import HTMLSession from requests_html
from requests_html import HTMLSession
import pandas as pd
from django.conf import settings
import urllib3
import idna
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import subprocess
from pathlib import Path
import os
settings.configure()


data = {
    'attempt_number': 1,
    'event':
        {
            'api_version': '2018-03-22',
            'created_at': '2021-06-27T10:52:11Z',
            'data':
                {
                    'id': 'e9149196-cb3a-40ab-aded-89b42992989f',
                    'code': '85KAWFXR',
                    'name': 'E-wallet Account Deposit For Tech Wise',
                    'pricing':
                        {
                            'dai':
                                {
                                    'amount': '39.976034367396745651',
                                    'currency': 'DAI'
                                },
                            'usdc':
                                {
                                    'amount': '40.000000',
                                    'currency': 'USDC'
                                },
                            'local':
                                {
                                    'amount': '40.00',
                                    'currency': 'USD'
                                },
                            'bitcoin':
                                {
                                    'amount': '0.00122586',
                                    'currency': 'BTC'
                                },
                            'ethereum':
                                {
                                    'amount': '0.021932000',
                                    'currency': 'ETH'
                                },
                            'litecoin':
                                {
                                    'amount': '0.31606811',
                                    'currency': 'LTC'
                                },
                            'bitcoincash':
                                {
                                    'amount': '0.08822037',
                                    'currency': 'BCH'
                                }
                        },
                    'checkout':
                        {
                            'id': 'e8f64a0a-e63c-401a-aff1-0dde24784cf3'
                        },
                    'metadata':
                        {
                            'email': 'teckwise@gmail.com'
                        },
                    'payments': [

                    ],
                    'resource': 'charge',
                    'timeline': [{'time': '2021-06-27T10:52:11Z', 'status': 'NEW'}],
                    'addresses': {'dai': '0x66475a28be4cdf98b1537d93ece9df4c88f6f9c8',
                                  'usdc': '0x66475a28be4cdf98b1537d93ece9df4c88f6f9c8',
                                  'bitcoin': '3DMZyJ9336ygBVx2734M1cC3YPLFvY33tE',
                                  'ethereum': '0x66475a28be4cdf98b1537d93ece9df4c88f6f9c8',
                                  'litecoin': 'MMX93KuUoU1e1QtcxjLVVsCSXqEpCbSzZm',
                                  'bitcoincash': 'qrcvdrr0ck6jcjapater6kk89cxl5jc9kguy8hrkeu'},
                    'created_at': '2021-06-27T10:52:11Z', 'expires_at': '2021-06-27T11:52:11Z',
                    'hosted_url': 'https://commerce.coinbase.com/charges/85KAWFXR',
                    'description': 'Payment for my trading wallet',
                    'pricing_type': 'fixed_price',
                    'support_email': 'wusetech@gmail.com',
                    'exchange_rates': {'BCH-USD': '453.41', 'BTC-USD': '32630.1', 'DAI-USD': '1.0005995', 'ETH-USD': '1823.795', 'LTC-USD': '126.555', 'USDC-USD': '1.0'},
                    'payment_threshold': {'overpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'},
                                          'overpayment_relative_threshold': '0.005',
                                          'underpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'},
                                          'underpayment_relative_threshold': '0.005'}
                },
            'id': '1a497b60-9ac5-44f5-acb8-13dd1be5d12d',
            'resource': 'event',
            'type': 'charge:created'
        },
    'id': '667eefb4-20b1-4b97-a21b-dd1e8b854a86',
    'scheduled_for': '2021-06-27T10:52:11Z'
}

amount = data['event']['data']['pricing']['local']['amount']
currency = data['event']['data']['pricing']['local']['amount']
checkout_id = data['event']['data']['checkout']['id']
email = data['event']['data']['description']
code = data['event']['data']['code']
event_type = data['event']['type']

btc_amount = data['event']['data']['pricing']['bitcoin']['amount']
btc_address = data['event']['data']['addresses']['bitcoin']

eth_amount = data['event']['data']['pricing']['ethereum']['amount']
eth_address = data['event']['data']['addresses']['ethereum']

lit_amount = data['event']['data']['pricing']['litecoin']['amount']
lit_address = data['event']['data']['addresses']['litecoin']

bch_amount = data['event']['data']['pricing']['bitcoincash']['amount']
bch_address = data['event']['data']['addresses']['bitcoincash']



data2 = {''
         'abbreviation': 'WAT',
         'client_ip': '197.210.85.243',
         'datetime': '2021-06-28T23:50:41.975923+01:00',
         'day_of_week': 1,
         'day_of_year': 179,
         'dst': False,
         'dst_from': None,
         'dst_offset': 0,
         'dst_until': None,
         'raw_offset': 3600,
         'timezone': 'Africa/Lagos',
         'unixtime': 1624920641,
         'utc_datetime': '2021-06-28T22:50:41.975923+00:00',
         'utc_offset': '+01:00',
         'week_number': 26
         }

date_data = (data2['datetime']).replace('T', ' ')[0:10]
created_datetime = (datetime.strptime(date_data, '%Y-%m-%d'))


data3 = {
    "motd":
        {
            "msg":"If you or your company use this project or like what we doing, please consider backing us so we can continue maintaining and evolving this project.",
            "url":"https://exchangerate.host/#/donate"
        },
    "success":'true',
    "query":
        {
            "from":"USD",
            "to":"NGN",
            "amount":50
        },
    "info":
        {
            "rate":410.158787
        },
    "historical":'false',
    "date":"2021-06-30",
    "result":20507.939351
}


charge_confirmed = {
    'attempt_number': 8,
    'event':
        {
            'api_version': '2018-03-22',
            'created_at': '2021-07-01T00:53:32Z',
            'data':
                {
                    'id': 'cb82bd0d-e382-4a18-a28b-ad857f8ef25e',
                    'code': 'HRNJF5BP',
                    'name': 'E-wallet Account Deposit For Daniel',
                    'pricing':
                        {
                            'dai':
                                {
                                    'amount': '2.997551931578329474',
                                    'currency': 'DAI'
                                },
                            'usdc':
                                {
                                    'amount': '3.000107',
                                    'currency': 'USDC'
                                },
                            'local':
                                {
                                    'amount': '1230.47',
                                    'currency': 'NGN'
                                },
                            'bitcoin': {'amount': '0.00008604', 'currency': 'BTC'}, 'ethereum': {'amount': '0.001334000', 'currency': 'ETH'}, 'litecoin': {'amount': '0.02097171', 'currency': 'LTC'},
                            'bitcoincash': {'amount': '0.00575395', 'currency': 'BCH'}
                        },
                    'checkout':
                        {'id': '434f7eb8-a7bf-41cd-8a63-525c9fcfe0b6'},
                    'metadata': {},
                    'payments':
                        [
                            {
                                'block':
                                        {
                                            'hash': '000000000000000000004035a3c30d5a95de69e7769ec065c180c63eccab7906',
                                            'height': 689260,
                                            'confirmations': 0,
                                            'confirmations_required': 1
                                            },
                                  'value':
                                      {
                                          'local': {'amount': '1230.50', 'currency': 'NGN'},
                                        'crypto': {'amount': '0.00008604', 'currency': 'BTC'}
                                      },
                                'status': 'CONFIRMED', 'network': 'bitcoin', 'detected_at': '2021-07-01T00:40:18Z',
                                'transaction_id': 'd83568e80b9318fee77037c54dd095d890ce53585ce941564773e7f42a34530a'}],
                    'resource': 'charge', 'timeline':
                    [{'time': '2021-07-01T00:24:14Z', 'status': 'NEW'},
                     {'time': '2021-07-01T00:40:18Z', 'status': 'PENDING',
                      'payment': {'value': {'amount': '0.00008604', 'currency': 'BTC'},
                                  'network': 'bitcoin', 'transaction_id': 'd83568e80b9318fee77037c54dd095d890ce53585ce941564773e7f42a34530a'}},
                     {'time': '2021-07-01T00:53:32Z', 'status': 'COMPLETED', 'payment': {'value': {'amount': '0.00008604', 'currency': 'BTC'},
                                                                                         'network': 'bitcoin',
                                                                                         'transaction_id': 'd83568e80b9318fee77037c54dd095d890ce53585ce941564773e7f42a34530a'}}],
                    'addresses': {'dai': '0x5205121662e22712a30e316f067829bb5e37ab4b',
                                  'usdc': '0x5205121662e22712a30e316f067829bb5e37ab4b',
                                  'bitcoin': '3CXBj8QVPG7C533dnVhiVqegkR7hypc6ka',
                                  'ethereum': '0x5205121662e22712a30e316f067829bb5e37ab4b',
                                  'litecoin': 'MSDazELPLkkFoNTorWeNnVQ4bkdWkEK3kB',
                                  'bitcoincash': 'qpmq4mwegnpxygc5yaux6lhdn7rkv5kstqe72943tt'},
                    'created_at': '2021-07-01T00:24:14Z',
                    'expires_at': '2021-07-01T01:24:14Z',
                    'hosted_url': 'https://commerce.coinbase.com/charges/HRNJF5BP',
                    'description': 'wusetech@gmail.com',
                    'confirmed_at': '2021-07-01T00:53:32Z',
                    'pricing_type': 'fixed_price',
                    'support_email': 'wusetech@gmail.com',
                    'exchange_rates': {'BCH-USD': '521.4',
                                       'BTC-USD': '34869.425',
                                       'DAI-USD': '1.0008525',
                                       'ETH-USD': '2249.47',
                                       'LTC-USD': '143.055',
                                       'USDC-USD': '1.0'
                                       },
                    'applied_threshold':
                        {'amount': '6.00',
                         'currency': 'NGN'
                         },
                    'organization_name': 'Doughs',
                    'payment_threshold': {'overpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'},
                                          'overpayment_relative_threshold': '0.005', 'underpayment_absolute_threshold':
                                              {'amount': '5.00', 'currency': 'USD'}, 'underpayment_relative_threshold': '0.005'},
                    'applied_threshold_type': 'ABSOLUTE'}, 'id': '60ae1238-5e08-4c62-bedf-d7d0520f1d6b',
            'resource': 'event', 'type': 'charge:confirmed'},
    'id': '153f596f-d30d-4fae-8230-a3f423d49862',
    'scheduled_for': '2021-07-01T01:26:26Z'}

# payments = (charge_confirmed['event']['data']['payments'])
#
# for i in payments:
#     print(i['value']['local']['amount'])

header = {
    'Date': 'Wed, 14 Jul 2021 06:09:38 GMT',
    'Content-Type': 'text/html; charset=UTF-8',
    'Transfer-Encoding': 'chunked',
    'Connection': 'keep-alive',
    'Cache-Control': 'public, max-age=300',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Dnt': '1',
    'Host': 'httpbin.org',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/83.0.4103.97 Safari/537.36',
    'X-Amzn-Trace-Id': 'Root=1-5ee7bbec-779382315873aa33227a5df6',
    'Content-Security-Policy': "frame-ancestors 'none'; "
                               "default-src 'none'; "                 
                               "connect-src https://commerce.coinbase.com https://api.commerce.coinbase.com https://www.coinbase.com https://api.amplitude.com/; font-src 'self';"
                               " img-src 'self' data: https://exceptions.coinbase.com/js https://res.cloudinary.com https://www.google-analytics.com/ https://images.coinbase.com; style-src 'self' 'unsafe-inline'; script-src 'self' https://www.googletagmanager.com https://www.google-analytics.com; report-uri https://commerce.coinbase.com/csp/report; block-all-mixed-content", 'Last-Modified': 'Tue, 29 Jun 2021 23:26:05 GMT', 'Referrer-Policy': 'strict-origin-when-cross-origin', 'Strict-Transport-Security': 'max-age=15552000; includeSubDomains', 'X-Content-Security-Policy': "frame-ancestors 'none'; default-src 'none'; connect-src https://commerce.coinbase.com https://api.commerce.coinbase.com https://www.coinbase.com https://api.amplitude.com/; font-src 'self'; img-src 'self' data: https://exceptions.coinbase.com/js https://res.cloudinary.com https://www.google-analytics.com/ https://images.coinbase.com; style-src 'self' 'unsafe-inline'; script-src 'self' https://www.googletagmanager.com https://www.google-analytics.com; report-uri https://commerce.coinbase.com/csp/report; block-all-mixed-content", 'X-Content-Type-Options': 'nosniff', 'X-DNS-Prefetch-Control': 'off', 'X-Download-Options': 'noopen', 'X-WebKit-CSP': "frame-ancestors 'none'; default-src 'none'; connect-src https://commerce.coinbase.com https://api.commerce.coinbase.com https://www.coinbase.com https://api.amplitude.com/; font-src 'self'; img-src 'self' data: https://exceptions.coinbase.com/js https://res.cloudinary.com https://www.google-analytics.com/ https://images.coinbase.com; style-src 'self' 'unsafe-inline'; script-src 'self' https://www.googletagmanager.com https://www.google-analytics.com; report-uri https://commerce.coinbase.com/csp/report; block-all-mixed-content", 'X-XSS-Protection': '1; mode=block', 'CF-Cache-Status': 'DYNAMIC', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
    'Server': 'cloudflare',
    'CF-RAY': '66e895545f4a06a6-LHR',
    'Content-Encoding': 'gzip'
}


dict1 = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
"Dnt": "1",
"Host": "httpbin.org",
"Upgrade-Insecure-Requests": "1",
'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

# create an HTML Session object
# session = HTMLSession()
url = 'https://commerce.coinbase.com/checkout/4ab2931f-7bca-4dc8-bd87-7b94f9c114c4'

# response = req.get('https://commerce.coinbase.com')
# dict2 = response.headers

# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    desired_capabilities={'browserName': 'htmlunit',
#                          'version': '2',
#                         'javascriptEnabled': True})
#

# driver.get("http://www.python.org")
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# assert "No results found." not in driver.page_source
# driver.close()

# if the script don't need output.
BASE_DIR = Path(__file__).resolve().parent.parent

a = os.path.join(BASE_DIR, 'coins')

data = {'attempt_number': 2, 'event': {'api_version': '2018-03-22', 'created_at': '2021-07-16T20:59:30Z', 'data': {'id': 'dc1d85f9-aaff-4e31-8e74-42d704562efb', 'code': '2RB74GHQ', 'name': 'E-wallet Account Deposit For Tech Wise', 'pricing': {'dai': {'amount': '49.952944326444489291', 'currency': 'DAI'}, 'usdc': {'amount': '50.000000', 'currency': 'USDC'}, 'local': {'amount': '50.00', 'currency': 'USD'}, 'bitcoin': {'amount': '0.00157009', 'currency': 'BTC'}, 'ethereum': {'amount': '0.026288000', 'currency': 'ETH'}, 'litecoin': {'amount': '0.40415471', 'currency': 'LTC'}, 'bitcoincash': {'amount': '0.11275228', 'currency': 'BCH'}}, 'metadata': {}, 'payments': [], 'resource': 'charge', 'timeline': [{'time': '2021-07-16T20:59:30Z', 'status': 'NEW'}], 'addresses': {'dai': '0x1acc9c7f3bcf324628d45c3ec039e2355c478d74', 'usdc': '0x1acc9c7f3bcf324628d45c3ec039e2355c478d74', 'bitcoin': '3JwrzYEpth11uTXvdz4srS5KZYuWeLSV1T', 'ethereum': '0x1acc9c7f3bcf324628d45c3ec039e2355c478d74', 'litecoin': 'MQJxN8fvRoyxKfKA4tUNG2c4NKkvywPat8', 'bitcoincash': 'qrm6xe59gf52m8jtdml46tsver3r7733p5k08a879e'}, 'created_at': '2021-07-16T20:59:30Z', 'expires_at': '2021-07-16T21:59:30Z', 'hosted_url': 'https://commerce.coinbase.com/charges/2RB74GHQ', 'brand_color': '#9BBF6A', 'description': 'donyemordi@gmail.com', 'pricing_type': 'fixed_price', 'support_email': 'wusetech@gmail.com', 'exchange_rates': {'BCH-USD': '443.45', 'BTC-USD': '31845.255', 'DAI-USD': '1.000942', 'ETH-USD': '1901.995', 'LTC-USD': '123.715', 'USDC-USD': '1.0'}, 'organization_name': 'Doughscoin limited', 'payment_threshold': {'overpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'}, 'overpayment_relative_threshold': '0.005', 'underpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'}, 'underpayment_relative_threshold': '0.005'}}, 'id': '59a90980-266e-4f77-a887-7bdf59e14c43', 'resource': 'event', 'type': 'charge:created'}, 'id': 'de7b78c8-7d28-434a-9fda-6f28c50a23df', 'scheduled_for': '2021-07-16T20:59:46Z'}

data2 = {
  "addresses": {
    "bitcoin": "3PMK9eJ2U28pUYy2RFrZZyyQXCjCs1zKgG",
    "bitcoincash": "qrn2rrmvzkhpwnpaz0y35erz7px07sahkye3ee2l76",
    "dai": "0x2feea025bc6e088ff10d68f9076b9c10764cb151",
    "ethereum": "0x2feea025bc6e088ff10d68f9076b9c10764cb151",
    "litecoin": "MWXFg9VJ7qQWzx6GnjQaV5yj8f48iwTyUG",
    "usdc": "0x2feea025bc6e088ff10d68f9076b9c10764cb151"
  },
  "brand_color": "#9BBF6A",
  "code": "GGHL3ZNR",
  "created_at": "2021-07-16T21:26:48Z",
  "description": "donyemordi@gmail.com",
  "exchange_rates": {
    "BCH-USD": "445.265",
    "BTC-USD": "31815.095",
    "DAI-USD": "1.0009875",
    "ETH-USD": "1902.03",
    "LTC-USD": "123.745",
    "USDC-USD": "1.0"
  },
  "expires_at": "2021-07-16T22:26:48Z",
  "hosted_url": "https://commerce.coinbase.com/charges/GGHL3ZNR",
  "id": "26ffb867-d060-48ce-aac7-9d219aebccaa",
  "metadata": {},
  "name": "E-wallet Account Deposit For Tech Wise",
  "organization_name": "Doughscoin limited",
  "payment_threshold": {
    "overpayment_absolute_threshold": {
      "amount": "5.00",
      "currency": "USD"
    },
    "overpayment_relative_threshold": "0.005",
    "underpayment_absolute_threshold": {
      "amount": "5.00",
      "currency": "USD"
    },
    "underpayment_relative_threshold": "0.005"
  },
  "payments": [],
  "pricing": {
    "bitcoin": {
      "amount": "0.00031432",
      "currency": "BTC"
    },
    "bitcoincash": {
      "amount": "0.02245854",
      "currency": "BCH"
    },
    "dai": {
      "amount": "9.990134741942331947",
      "currency": "DAI"
    },
    "ethereum": {
      "amount": "0.005258000",
      "currency": "ETH"
    },
    "litecoin": {
      "amount": "0.08081135",
      "currency": "LTC"
    },
    "local": {
      "amount": "10.00",
      "currency": "USD"
    },
    "usdc": {
      "amount": "10.000000",
      "currency": "USDC"
    }
  },
  "pricing_type": "fixed_price",
  "resource": "charge",
  "support_email": "wusetech@gmail.com",
  "timeline": [
    {
      "status": "NEW",
      "time": "2021-07-16T21:26:48Z"
    }
  ]
}

print(data2['code'])

pending = {
    'attempt_number': 6, 'event':
        {
            'api_version': '2018-03-22', 'created_at': '2021-07-24T06:52:25Z',
            'data':
                {'id': 'fecb23b6-92ae-4e78-97e3-7764f26a369e',
                 'code': 'NAB45HKP',
                 'name': 'E-wallet Account Deposit For Alexander',
                 'pricing':
                     {'dai': {'amount': '0.998930644744800691', 'currency': 'DAI'},
                      'usdc': {'amount': '1.000000', 'currency': 'USDC'},
                      'local': {'amount': '1.00', 'currency': 'USD'},
                      'bitcoin': {'amount': '0.00002950', 'currency': 'BTC'},
                      'ethereum': {'amount': '0.000466000', 'currency': 'ETH'},
                      'litecoin': {'amount': '0.00784375', 'currency': 'LTC'},
                      'bitcoincash': {'amount': '0.00217460', 'currency': 'BCH'}},
                 'metadata': {},
                 'payments': [{'block': {'hash': None, 'height': None, 'confirmations': 0, 'confirmations_required': 1},
                               'value': {'local': {'amount': '1.00', 'currency': 'USD'},
                                         'crypto': {'amount': '0.00002950', 'currency': 'BTC'}},
                               'status': 'PENDING',
                               'network': 'bitcoin',
                               'detected_at': '2021-07-24T06:52:25Z',
                               'transaction_id': '0cae5a98948730e999e3d13a69622df174b494088a6cba3d6d77a8844b85702e'}],
                 'resource': 'charge', 'timeline': [{'time': '2021-07-24T06:49:14Z', 'status': 'NEW'}, {'time': '2021-07-24T06:52:25Z', 'status': 'PENDING', 'payment': {'value': {'amount': '0.00002950', 'currency': 'BTC'}, 'network': 'bitcoin', 'transaction_id': '0cae5a98948730e999e3d13a69622df174b494088a6cba3d6d77a8844b85702e'}}], 'addresses': {'dai': '0x28bf16411431f1ece958b3bfb0d075682df669e5', 'usdc': '0x28bf16411431f1ece958b3bfb0d075682df669e5', 'bitcoin': '3Ps6GpfLxQ7Vc8cGX8QxRdchvS5tFyquo2', 'ethereum': '0x28bf16411431f1ece958b3bfb0d075682df669e5', 'litecoin': 'MBfXqKfHhgobmHCRrntPSvp4KyxMkqW1fW', 'bitcoincash': 'qr6zxd280hq69mhmdwadlcxgsmxu58jhn5zn9n398a'}, 'created_at': '2021-07-24T06:49:14Z', 'expires_at': '2021-07-24T07:49:14Z', 'hosted_url': 'https://commerce.coinbase.com/charges/NAB45HKP', 'brand_color': '#9BBF6A', 'description': 'wusetech@gmail.com', 'pricing_type': 'fixed_price', 'support_email': 'wusetech@gmail.com', 'exchange_rates': {'BCH-USD': '459.855', 'BTC-USD': '33899.975', 'DAI-USD': '1.0010705', 'ETH-USD': '2143.8', 'LTC-USD': '127.49', 'USDC-USD': '1.0'}, 'organization_name': 'Doughscoin limited', 'payment_threshold': {'overpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'}, 'overpayment_relative_threshold': '0.005', 'underpayment_absolute_threshold': {'amount': '5.00', 'currency': 'USD'}, 'underpayment_relative_threshold': '0.005'}}, 'id': '5e1bfa9b-aad2-499c-ad2f-4bc74849a2f1', 'resource': 'event', 'type': 'charge:pending'}, 'id': '1b88a9d4-8cec-4661-b620-8c0e548ce752', 'scheduled_for': '2021-07-24T07:00:30Z'}