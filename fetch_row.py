import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM courses;")
a = cursor.fetchone()               #return one row at a time
print(a)
conn.commit()