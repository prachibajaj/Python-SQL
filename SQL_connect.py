import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE if not exists courses(number INTEGER PRIMARY KEY, name text,etcs real);""")
#cursor.execute("""INSERT INTO courses VALUES ("02822","Python programming",5);""")
#conn.commit()
course = ("02457","Nonlinear Signal Processing",10)
cursor.execute("INSERT INTO courses VALUES(?,?,?);",course)
conn.commit()