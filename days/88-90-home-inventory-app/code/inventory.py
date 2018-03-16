#!python3

import sqlite3
import sys
from contextlib import contextmanager

DB = "Inventory.db"

#Script that creates the DB on first launch, otherwise is just a check.
def first_launch():
    try:
        conn = sqlite3.connect(DB)
    except:
        sys.exit('Error code X')

        
#generator to yield a db cursor and close the connection nicely.
@contextmanager
def access_db():
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()


#A somewhat dirty menu. Improvement Point (make it a dict perhaps)
def main_menu():
    menu = {}
    menu['1'] = "Add Room."
    menu['2'] = "Add Inventory."
    menu['3'] = "View Inventory List."
    menu['4'] = "Total Value."
    menu['5'] = "Exit."
    while True:
        print("\n")
        for item, desc in sorted(menu.items()):
            print(item, desc)

        choice = input("Selection: ")
        if choice == '1':
            add_room()
        elif choice == '2':
            add_inventory(check_input())
        elif choice == '3':
            view_inventory(check_input())
        elif choice == '4':
            calc_total()
        elif choice == '5':
            sys.exit()
        else:
            print("Invalid option, try again.")


#Adds a room. Scrubs the input first to only allow default chars.
def add_room():
    name = input("\nWhat name would you like to give the room? ")
    name = scrub(name)
    with access_db() as cursor:
        cursor.execute("CREATE TABLE '" + name.lower() + "' """"
                                    (Item TEXT, Value REAL)
                                    """)
        print("\nA room with name %s has been added to the db.\n" % name)


#Parses the DB for table names and returns a list of the names.
def list_rooms():
    room_list = []
    with access_db() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for room in cursor:
            room_list.append(room[0])
    return room_list


#The scrubbing function. Removes all chars that aren't letters and numbers.
def scrub(table_name):
    return ''.join( chr for chr in table_name if chr.isalnum() )


#Checks the users' input to see if it matches a room/table name.
def check_input():
    while True:
        print('\n')
        for room in list_rooms():
            print(room)
        selection = input('Select a room: ').lower()
        if selection not in list_rooms():
            print("\n%s does not exist." % selection)
        else:
            return scrub(selection)


#Allows users to add an item and value to the DB of a specific room.
def add_inventory(selection):
    while True:
        name = input("\nName of item: ")
        cost = input("Monetary value: ")
        with access_db() as cursor:
            cursor.execute("INSERT INTO '" + selection + "' VALUES(?, ?)", [name, cost])

        cont = input('\nHit Q to quit or any other key to continue: ')
        if cont.lower() == 'q':
            break


#Returns a list of all items in a room and their total value.
def view_inventory(selection):
    total = 0
    with access_db() as cursor:
        cursor.execute("SELECT * FROM '" + selection + "'")
        print("\n")
        for data in cursor:
            print("%s: $%d" % (data[0], data[1]))
            total += data[1]
        print("Total Value: $%d" % total)


#Function to calculate the $ total of the entire database.
def calc_total():
    total = 0
    room_list = list_rooms()
    with access_db() as cursor:
        for room in room_list:
            cursor.execute("SELECT value FROM '" + room + "'")
            for value in cursor:
                total += value[0]
    print("\nTotal Value of all rooms: $%d" % total)


if __name__ == "__main__":
    first_launch()
    main_menu()
