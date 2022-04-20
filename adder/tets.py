import csv
import os
from pathlib import Path
from client import csv_data
# read_csv function which is used to read the required CSV file
BASE_DIR = Path(__file__).resolve().parent.parent

csv_data = csv_data

def main(user_id):
    # 1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlist = []
    with open(csv_data, newline="") as f:
        reader = csv.reader(f)
        # id_hash = input("Enter the username of the user you wish to remove from file:")
        id_hash = str(user_id)

        for row in reader:  # for every row in the file

            if row[0] != id_hash:  # as long as the username is not in the row .......
                updatedlist.append(row)  # add each row, line by line, into a list called 'udpatedlist'
        updatefile(updatedlist)

def updatefile(updatedlist):
    with open(csv_data, "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")

main(user_id="")