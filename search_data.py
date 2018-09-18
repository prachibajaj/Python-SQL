import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM courses WHERE number = ? OR name = ? OR etcs = ?",("02451","None","5.0"))
rows = cursor.fetchall()
print(rows)
conn.commit()
