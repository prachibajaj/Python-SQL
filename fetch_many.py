 import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM courses;")
for row in cursor: 
    print(row)
conn.commit()