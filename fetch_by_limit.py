import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM courses ORDER BY number LIMIT 2;")
c = cursor.fetchall()
print(c)
conn.commit()
