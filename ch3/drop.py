import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''drop table students;''')
print("Table Dropped successfully")

conn.close()
