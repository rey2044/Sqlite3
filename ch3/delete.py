import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")

conn.execute('''DELETE FROM students where id=1;''')
conn.commit()
print("Data Deleted successfully")
conn.close()