import time
import requests
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import (View, TemplateView, ListView, DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from mailjet_rest import Client
from token_generator import *
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from uuid import getnode as get_mac
from generate_password import generated_password
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout
from notification import *
from django.db.models import Q
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from percent_calculator import percentage_calculator
from deposit_id import *
from decimal import Decimal
from userwallet.flutter_wave_deposit_api import transfer_deposit, deposit_api, withdraw, verify_transanction
from user.models import *
from app.models import *
# vtuApp
# from vtuApp.models import *
# from vtuApp.honourworldApi import *
from userwallet.models import *
from myadmin.models import *
from transaction_id import *
import datetime
from datetime import *
from referral.models import *
import json
import socket
import json
import random
import pickle
import csv
from pickle_load import *
from notification import *
from gb_calculator import *


try:
    admin = Administration.objects.get(user__top_admin=True)
    if admin.site_available == True:
        registration_mess = admin.available_message
    else:
        registration_mess = admin.not_available_message

    if admin.live_bot == True:
        group = general_grp
    else:
        group = private_grp

    if admin.flutter_wave == 'nexzus':
        FLUTTER_WAVE_SECRET_KEY = settings.FLUTTER_WAVE_SECRET_KEY2
    else:
        FLUTTER_WAVE_SECRET_KEY = settings.FLUTTER_WAVE_SECRET_KEY
except:
    admin = ''

current_timezone = datetime.now() + timedelta(hours=1)
api_key = settings.MAIL_JET_API_KEY
api_secret = settings.MAIL_JET_API_SECRET_KEY
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
COMPANY = 'Lift9ja Ltd'
success = '✓'
web_logins_bot = '2050752630:AAEOGwpb9k0KBdT8qF0EUhnbLlexMjx9PzY'
web_login_page = '-621761649'
bot_id = '5149735788:AAHF9THgzU7BDTwC6aPckHOsGgaOH1s1ocA'
# groups
private_grp = '-649094803'
payment_grp = 'payusersnotifyer'

minimum = 1000
minimum_withdrawal = 99
maximum = 700000
file_name = 'coupons/coupon_codes'
site_name = 'lift9ja'
lst = []
filename = 'faker'
def get_name(data):
    name = []
    with open(r'names.csv', encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['name'] = row[0]
            name.append(user)


    infile = open(filename, 'rb')
    new_dict = pickle.load(infile)
    infile.close()

    for key in new_dict:
        num = new_dict[key]
        lst.append(num)
    highest = max(lst)

    get_num = highest
    faker = new_dict

    print(faker)

    if get_num >= len(name):
        datas = {'reg': 1, 'login': 0, 'deposit': 0,
                 'create_plan': 0, 'daily_earning': 0,
                 'plan_ended': 0, 'withdraw': 0,
                 'withdraw_sent': 0
                 }
        outfile = open(filename, 'wb')
        pickle.dump(datas, outfile)
        outfile.close()

        return name[0]['name']

    else:

        faker[data] = get_num + 1
        print(faker[data])

        outfile = open(filename, 'wb')
        pickle.dump(faker, outfile)
        outfile.close()

        name = name[faker[data]]['name']
        print(name)
        return name
