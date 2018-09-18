import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM courses WHERE number =?",('02820',))
cursor.execute("SELECT * FROM courses")
print(cursor.fetchall())
conn.commit()