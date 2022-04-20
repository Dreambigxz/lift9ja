from telethon.sync import TelegramClient
from telethon.tl.types import (
    InputPeerUser, UserStatusOffline, UserStatusRecently,
    UserStatusLastWeek, UserStatusLastMonth
)
from telethon.errors.rpcerrorlist import PeerFloodError
import sys
import csv
import random
import time
import client
from client import main2
import os
import pickle
import pyfiglet
import datetime
from colorama import init, Fore
from pathlib import Path

csv_data = client.csv_data2


init()

lg = Fore.LIGHTGREEN_EX
rs = Fore.RESET
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN


info = lg + '(' + w + 'i' + lg + ')' + rs
error = lg + '(' + r + '!' + lg + ')' + rs
success = w + '(' + lg + '+' + w + ')' + rs
INPUT = lg + '(' + cy + '~' + lg + ')' + rs
colors = [lg, w, r, cy]
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('Genisys')
    print(random.choice(colors) + logo + rs)

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clr()
banner()
print(f'  {r}Version: {w}2.5 {r}| Author: {w}Cryptonian{rs}\n')


f = open('vars.txt', 'rb')
accs = []
while True:
    try:
        accs.append(pickle.load(f))
    except EOFError:
        f.close()
        break
print(f'{INPUT}{cy} Choose an account to add with\n')
i = 0

for acc in accs:
    print(f'{lg}({w}{i}{lg}) {acc[2]}')
    i += 1
ind = int(input(f'\n{INPUT}{cy} Enter choice: '))
api_id = accs[ind][0]
api_hash = accs[ind][1]
phone = accs[ind][2]
client = TelegramClient(f'sessions\\{phone}', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

users = []
with open(csv_data, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

mode = int(input("Enter 1 to send by user ID or 2 to send by username: "))

messages = ["Good day {}, "
            "have you heard of Doughscoin limited company? "

            'This is not like other investment platform, i was introduced by a friend in uk and i observerd for days before joining, I have been'
            ' enjoying the system for weeks now so i decided to let other people know about it, and also make some ref money too.\n\n'
            
             "Amazing offer available for both old and new user sponsored by their partners.\n"
            "So if you sign up now you get a welcome bonus, which is also tradable.\n\n"
            
            "You can join the officially discussion group here.\n"
            "https://t.me/doughscoin\n\n"

            "Site Link\n"
            "https://www.doughscoin.com\n\n"
            ""

            ]

n = 0
flood = 0

for user in users:

    if n == 55:
        print('sleeping for 30mins....', datetime.datetime.now())
        time.sleep(2000)
        n -= n
        flood -= flood
    else:
        print('Message sent: ', n)

    if mode == 2:
        if user['username'] == "":
            continue
        receiver = client.get_input_entity(user['username'])
    elif mode == 1:
        receiver = InputPeerUser(user['id'],user['access_hash'])
    else:
        print("Invalid Mode. Exiting.")
        client.disconnect()
        sys.exit()
    message = random.choice(messages)
    try:
        print("Sending Message to:", user['name'])
        client.send_message(receiver, message.format(user['name']))
        main2(user['id'])
        n += 1
        print("Waiting for 60-80 Seconds...")
        time.sleep(random.randrange(60, 80))

    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        flood += 1
        print('flood error: ', flood)
        if flood == 30:
            client.disconnect()
            sys.exit()
    except Exception as e:
        print("Error:", e)
        print("Trying to continue...")
        continue
client.disconnect()
print("Done. Message sent to all user.")