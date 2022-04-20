import csv
import os
from pathlib import Path

# read_csv function which is used to read the required CSV file
BASE_DIR = Path(__file__).resolve().parent.parent


# csv_data = os.path.join(BASE_DIR, 'Genisys/rooms/users3.csv')
csv_data = os.path.join(BASE_DIR, 'adder/rooms/1.csv')

def main(username):
    # 1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlist = []
    with open(csv_data, newline="") as f:
        reader = csv.reader(f)
        # id_hash = input("Enter the username of the user you wish to remove from file:")
        id_hash = str(username)

        for row in reader:  # for every row in the file

            if row[0] != id_hash:  # as long as the username is not in the row .......
                updatedlist.append(row)  # add each row, line by line, into a list called 'udpatedlist'
        updatefile(updatedlist)

def updatefile(updatedlist):
    with open(csv_data, "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")

def main2(user_id):
    # 1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlist = []
    with open(csv_data2, newline="") as f:
        reader = csv.reader(f)
        # id_hash = input("Enter the username of the user you wish to remove from file:")
        id_hash = str(user_id)

        for row in reader:  # for every row in the file

            if row[1] != id_hash:  # as long as the username is not in the row .......
                updatedlist.append(row)  # add each row, line by line, into a list called 'udpatedlist'
        updatefile2(updatedlist)

def updatefile2(updatedlist):
    with open(csv_data2, "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")

"""
Accounts

0 = smeek
1 thomas
2 lawrence

3 vicky
4 Gabriel
5 james anderson
6 felix
7 frances elia
8 franklin
9 joseph


currently using
1,2,8
"""


#great
# api_id = 7948050
# api_hash = ''
# phone = '+14847676053'

#Agent mark
# api_id = 7812967
# api_hash = 'c0517d2f7b73c65ea4cb9ec96f3978b3'
# phone = '+2348107340034'

#@gregory
# api_id = 7795970
# api_hash = 'd4199ecd7fae3b4a1de4e55b75d40967'
# phone = '+37120494486'

#noky
# api_id = 7038206
# api_hash = 'af6a3aa54d3dc0f9d28c2a131ff4ba6d'
# phone = '+2349028656624'


#jackson
# api_id = 7979162
# api_hash = '8673eac2f96cb1f2ce63428c3db93cc3'
# phone = '+2349082910686'


#Juliet
# api_id = 7640990
# api_hash = '22b11c0abf96b59804fa7f1b7ff6f0df'
# phone = '+2347037401896'

#Smeak
api_id = 7640990
api_hash = '22b11c0abf96b59804fa7f1b7ff6f0df'
phone = '+2347037401896'

#dany
# api_id = 4691786
# api_hash = 'eac51d3601bec214c16316831061ab13'
# phone = '+2348167997730'

"""
4713000
5f6b676cf607274da5a99b73197a7e00
+23409090559922

Ruth
+1 561 703-9769
7032681
4e62170b5249bf8d02983f6b51791787

Emmanuel
7400647
f8649eea1f623f16a54dc2ea4f2c17dd
+234 706 204-842-6

Fedrick
7375027
681af7853b1d2acae18d9d8720c7b197
+7 965 854-41-07

Thomas 
7973100
32b42f703dddd07bfc085235d8e682f7
+91 97071 14892

cymthia
7748677
2cfd3151444e6adfc6b81f9d0385f27b
+234 907 631-381-5








"""