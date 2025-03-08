from jinja2_sites.test_jinja import get_name_from_class
import sqlite3
#вывод всех ресторанов через классы
from test_class.classis import *
con=sqlite3.connect('test.db')
curs=con.cursor()
curs.execute('SELECT * FROM table_class')
c=curs.fetchall()
for i in c:
    f=get_name_from_class(i)
    print(f)
con.commit()
con.close()


#добавление ресторанов через классы
#r2 = Restaurant('106', "Balkan", "3", '4', '5', '6', '7', '8', '9', '10')
#atr = list(r2.__dict__.keys())
#val = list(r2.__dict__.values())
#table_name = 'table_class'
#con = sqlite3.connect('test.db')
#curs = con.cursor()
#curs.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
# {atr[0]} INTEGER PRIMARY KEY,
# {atr[1]} TEXT NOT NULL,
# {atr[2]} TEXT NOT NULL,
# {atr[3]} TEXT NOT NULL,
# {atr[4]} TEXT NOT NULL,
# {atr[5]} TEXT NOT NULL,
# {atr[6]} TEXT NOT NULL,
# {atr[7]} TEXT NOT NULL,
# {atr[8]} TEXT NOT NULL,
# {atr[9]} TEXT NOT NULL
# )
#''')
#curs.execute(
#    f'INSERT INTO {table_name} ({", ".join([ atr[1], atr[2], atr[3], atr[4], atr[5], atr[6], atr[7], atr[8], atr[9]])}) VALUES (?,?,?,?,?,?,?,?,?)',
#    ( val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9])
#)
#con.commit()
#con.close()

#удаление ресторанов через классы
#r3=Restaurant('67', "Balkan", "3", '4', '5', '6', '7', '8', '9', None)
#atr = list(r3.__dict__.keys())
#val = list(r3.__dict__.values())
#table_name = 'table_class'
#con = sqlite3.connect('test.db')
#curs = con.cursor()
#curs.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
# {atr[0]} INTEGER PRIMARY KEY,
# {atr[1]} TEXT NOT NULL,
# {atr[2]} TEXT NOT NULL,
# {atr[3]} TEXT NOT NULL,
# {atr[4]} TEXT NOT NULL,
# {atr[5]} TEXT NOT NULL,
# {atr[6]} TEXT NOT NULL,
# {atr[7]} TEXT NOT NULL,
# {atr[8]} TEXT NOT NULL,
# {atr[9]} TEXT NOT NULL
# )
#''')
#curs.execute(f'DELETE FROM {table_name} WHERE {atr[1]} = ?', (val[1],))
#con.commit()
#con.close()