import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE students (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    rno INTEGER NOT NULL
);''')
print("Table created successfully")

conn.close()
