import sqlite3
from tkinter.tix import TEXT

conn= sqlite3.connect("flask_api.db")

print("opened the database")

conn.execute("CREATE TABLE users (id INT ,name TEXT, email TEXT, phone TEXT, role TEXT, password TEXT)")

print ("table created successfully")

conn.close()