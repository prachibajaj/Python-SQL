import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("UPDATE courses SET name=?, etcs = ? WHERE number = ?",('Hello World','7','02454'))
cursor.execute("SELECT * FROM courses")
print(cursor.fetchall())
conn.commit()
