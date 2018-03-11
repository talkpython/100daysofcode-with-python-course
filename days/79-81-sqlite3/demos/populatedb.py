#!python3

import sqlite3

def enter_details():
    while True:
        info = []
        name = input('Enter a name: ')
        address = input('Enter an address: ')
        number = input('Enter a phone number: ')
        for i in (name, address, number):
            info.append(i)

        with sqlite3.connect("addressbook.db") as connection:
            c = connection.cursor()
            c.execute("INSERT INTO Details VALUES(?, ?, ?)", info)
            print('Data inserted to database.\n')
            
        stop = input("Hit Q to to quit.\n")
        if stop.upper() == 'Q':
            break
        else:
            continue

if __name__ == "__main__":
    enter_details()
