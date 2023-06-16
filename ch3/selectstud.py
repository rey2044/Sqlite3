import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")

curr=conn.execute('''SELECT id, name, rno
FROM students;''')

# Print the retrieved data
for row in curr:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Roll No:", row[2])
    print("")
print("Data printed successfully")
# Close the database connection
conn.close()
