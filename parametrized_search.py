import sqlite3 as sq
conn = sq.connect("courses.db")
cursor = conn.cursor()
param = {'etcs':5.0}
cursor.execute("SELECT number FROM courses WHERE etcs=?",(param['etcs'],))
rows = cursor.fetchall()
print(rows)
conn.commit()