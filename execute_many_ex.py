import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE if not exists courses(number INTEGER PRIMARY KEY, name text,etcs real);""")
course = [("02454","Introduction to cognitive science",5),("02451","Digital Signal Processing",10)]
cursor.executemany("INSERT INTO courses VALUES(?,?,?);",course)


conn.commit()