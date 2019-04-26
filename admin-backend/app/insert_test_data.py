import sys
import os

from database import Database

from datetime import datetime
from insert_test_counties import counties


surnames = ["X", "Y"]
names = ["Popescu", "Ionescu"]

months_b = [1, 5, 7, 9, 11]
months_d = [2, 3, 6, 9, 12]

now = datetime.now()
pin = 0

def inser_test_data():
    for _, (city, _, _, _) in counties.items():
        for i in range(5):
            surname = "{}{}".format(surnames[i % 2], i)
            name = "{}{}".format(names[i % 2], i)

            date_b = now
            while True:
                try:
                    date_b = date_b.replace(month=months_b[i])
                    break
                except:
                    date_b = date_b.replace(day=date_b.day-1)
            
            date_d = now
            while True:
                try:
                    date_d = date_d.replace(month=months_d[i])
                    break
                except:
                    date_d = date_d.replace(day=date_d.day-1)

            Database.insert_birth(pin, surname, name, date_b, city)
            Database.insert_death(pin, date_d, city)

            pin += 1

if __name__ == '__main__':
    inser_test_data()
    
