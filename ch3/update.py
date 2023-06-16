import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('''UPDATE students
SET name = 'John Smith', rno = 54321
WHERE id = 1;''')
conn.commit()
print("Data Inserted successfully")
conn.close()