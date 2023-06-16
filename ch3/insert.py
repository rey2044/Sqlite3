import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('''INSERT INTO students (id, name, rno)
VALUES (1, 'Rey Patel', 12345);''')
conn.commit()
print("Data Inserted successfully")
conn.close()