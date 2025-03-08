import sqlite3
from pandas.io.sql import execute

connection = sqlite3.connect("test.db")
curs = connection.cursor()
curs.execute('PRAGMA foreign_keys = ON;') #поддержка внешнего ключа

#cursor.execute('''
#CREATE TABLE  IF NOT EXISTS Izuminka (
#id_izu INTEGER PRIMARY KEY,
#izuminka TEXT NOT NULL);
#''')
#cursor.execute('''
#CREATE TABLE IF NOT EXISTS test (
#id_test INTEGER PRIMARY KEY,
#название TEXT NOT NULL,
#izuminka TEXT NOT NULL);
#''')

curs.execute('SELECT izuminka FROM test')
b=curs.fetchall()
curs.execute('SELECT * FROM Izuminka')
c=curs.fetchall()
tim_res_izu=[]
print(c)
#for i in b:
#    i=list(map(int,"".join(i).split()))
#    tim_res_izu.append(i)
#c_dict=dict((x,y) for x,y in c)
#for g in tim_res_izu:
#    for h in g:
#        if h in c_dict.keys():
#            print(c_dict[h])






connection.commit()
connection.close()