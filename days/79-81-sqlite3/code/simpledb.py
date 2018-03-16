#!python3

import sqlite3

connection = sqlite3.connect('addressbook.db')

c = connection.cursor()

c.execute("""CREATE TABLE Details
(name TEXT, address TEXT, phone_number INT)
""")

connection.close()
