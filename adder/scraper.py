from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import (
    InputPeerUser, UserStatusOffline, UserStatusRecently,
    UserStatusLastWeek, UserStatusLastMonth, InputPeerEmpty, UserStatusOnline,
)
import datetime
import pytz
import os
import sys
import csv
import traceback
import time
import client
import random
from client import main
import os
import pickle
import pyfiglet
import datetime
from datetime import date, timedelta
from colorama import init, Fore
from pathlib import Path
csv_data = client.csv_data


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
print(f'{INPUT}{cy} Choose an account to scrab with\n')
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

utc=pytz.UTC
BASE_DIR = Path(__file__).resolve().parent.parent
path = os.path.join(BASE_DIR, 'Genisys/rooms')

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

chats = []
last_date = None
chunk_size = 200
groups = []
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    print(chat)
    try:
        if chat.megagroup == True or chat.megagroup == False:
            pass
        groups.append(chat)
    except:
        continue

print('Choose a group to scrape members from:')
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Enter a Number: ")
target_group = groups[int(g_index)]

group_name = (target_group.title)
print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Saving In file...')
with open("{}/{} .csv".format(path, group_name),"w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
            name = (first_name + ' ' + last_name).strip()
            if user.id == 1940050024:
                pass
            else:
                writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
    print(' Members scraped successfully.')
