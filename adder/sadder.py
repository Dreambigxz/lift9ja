from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import (PeerFloodError, UserPrivacyRestrictedError,
                                          UserChannelsTooMuchError, UserKickedError, FloodWaitError,
                                          UsernameOccupiedError, UserBlockedError, UserNotMutualContactError)
from telethon.tl.functions.channels import InviteToChannelRequest
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
from colorama import init, Fore
from pathlib import Path
csv_data = client.csv_data

#https://github.com/amanbytes/auto-add-members-in-telegram-groups-and-channels/blob/main/auto-add.py

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


f = open('adder/vars.txt', 'rb')
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


def add_users_to_group():
    users = []
    with open(csv_data, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['username'] = row[0]
            try:
                user['id'] = (row[1])
                user['access_hash'] = (row[2])
            except IndexError:
                print('user without id or access_hash')
            users.append(user)

    random.shuffle(users)
    chats = []
    last_date = None
    chunk_size = 10
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup == True:  # Condition To Only List Megagroups
                groups.append(chat)
        except:
            continue

    print('Choose a group to add members:')

    i = 0
    for group in groups:
        print(str(i) + '- ' + group.title)
        i += 1

    g_index = input("Enter a Number: ")
    target_group = groups[int(g_index)]
    print('\n\nChosen Group:\t' + groups[int(g_index)].title)

    target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

    mode = int(input("Enter 1 to add by username or 2 to add by ID: "))

    error_count = 0

    n = 0

    for user in users:
        if n >= 95:
            sys.exit('Done....')

        try:
            print("Adding {}".format(user['username']))
            if mode == 1:
                if user['username'] == "":
                    continue
                user_to_add = client.get_input_entity(user['username'])
            elif mode == 2:
                user_to_add = InputPeerUser(user['id'], user['access_hash'])
            else:
                sys.exit("Invalid Mode Selected. Please Try Again.")

            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            n += 1
            print(n)


            try:
                main(user['username'])
            except:
                pass

            print("Waiting 80 Seconds...")
            time.sleep(80)



        except PeerFloodError:
            print("Getting Flood Error from Telegram. You should stop script now.Please try again after some time.")
            sys.exit('Flood error....')

        except UserPrivacyRestrictedError:
            print("The user's privacy settings do not allow you to do this. Skipping.")
            main(user['username'])

        except UserChannelsTooMuchError:
            print('user channel is too much')
            main(user['username'])
            continue
        except InviteToChannelRequest:
            main(user['username'])
            continue
        except UserKickedError:
            main(user['username'])
            continue
        except FloodWaitError:
            sys.exit('Flood error....')
        except UsernameOccupiedError:
            main(user['username'])
            print("Invalid username")
        except UserBlockedError:
            main(user['username'])
            print("User Blocked")
        except UserNotMutualContactError:
            main(user['username'])
            print("User Not inn contact")
        except:
            main(user['username'])
            traceback.print_exc()
            print("Unexpected Error")
            error_count += 1
            print(error_count)
            if error_count > 10:
                sys.exit('too many errors')
            continue



add_users_to_group()

