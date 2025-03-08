import sqlite3
from aiogram import *
import sqlite3
from test_class.classis import *


#def save_izu(path:str,name_table:str,name:str):
#    try:
#        connection = sqlite3.connect(path)
#        curs = connection.cursor()
#        if isinstance(name,str):
#            curs.execute(f'INSERT INTO Izuminka (izuminka) VALUES (?)',(name,))
#            connection.commit()
#    except sqlite3.Error:
#        print('Ошибка в СУБД')
#    except  name.isdigit:
#        print('Ошибка, вы ввели число, надо строку')
#    finally:
#        connection.close()
        
def dobav_zav(r2:Restaurant):
    #обработай на ошибке(если чел отправит фотку с данными или файл,если смайлик,и т.д)
    atr = list(r2.__dict__.keys())
    val = list(r2.__dict__.values())
    table_name = 'table_class'
    con = sqlite3.connect('test.db')
    curs = con.cursor()
    curs.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
     {atr[0]} INTEGER PRIMARY KEY,
     {atr[1]} TEXT NOT NULL,
     {atr[2]} TEXT NOT NULL,
     {atr[3]} TEXT NOT NULL,
     {atr[4]} TEXT NOT NULL,
     {atr[5]} TEXT NOT NULL,
     {atr[6]} TEXT NOT NULL,
     {atr[7]} TEXT NOT NULL,
     {atr[8]} TEXT NOT NULL,
     {atr[9]} TEXT NOT NULL
     )
    ''')
    curs.execute(
        f'INSERT INTO {table_name} ({", ".join([ atr[1], atr[2], atr[3], atr[4], atr[5], atr[6], atr[7], atr[8], atr[9]])}) VALUES (?,?,?,?,?,?,?,?,?)',
        ( val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9])
    )
    con.commit()
    con.close()

#def del_zav(path,name_table,name_zav):
#    try:
#        con=sqlite3.connect(path)
#        curs=con.cursor()
#        curs.execute(f'DELETE FROM {name_table} WHERE название = ?',(name_zav,))
#        con.commit()
#    except sqlite3.Error:
#        print('Ошибка в СУБД')
#    finally:
#        con.close()
#



def f_split(x):
    s1 = x.split()[1:]
    s1 = ''.join(s1)
    return s1
def chek_digit(s):
    for i in s:
        if i.isdigit():
            return True
    return False

def show_restaraunt(path):
    try:
        con=sqlite3.connect(path)
        curs=con.cursor()
        curs.execute('SELECT name FROM table_class')
        res_name=[row[0] for row in curs.fetchall()]
        return res_name
    except sqlite3.Error:
        print('Ошибка в СУБД')
    finally:
        con.close()

def del_zav(r3:Restaurant):
    atr = list(r3.__dict__.keys())
    val = list(r3.__dict__.values())
    table_name = 'table_class'
    con = sqlite3.connect('test.db')
    curs = con.cursor()
    curs.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
     {atr[0]} INTEGER PRIMARY KEY,
     {atr[1]} TEXT NOT NULL,
     {atr[2]} TEXT NOT NULL,
     {atr[3]} TEXT NOT NULL,
     {atr[4]} TEXT NOT NULL,
     {atr[5]} TEXT NOT NULL,
     {atr[6]} TEXT NOT NULL,
     {atr[7]} TEXT NOT NULL,
     {atr[8]} TEXT NOT NULL,
     {atr[9]} TEXT NOT NULL
     )
    ''')
    curs.execute(f'DELETE FROM {table_name} WHERE {atr[1]} = ?', (val[1],))
    con.commit()
    con.close()

def poisk_for_id(r2:Restaurant):
    name_zav=r2.name
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM table_class')
    b=cur.fetchall()
    con.close()
    for i in b :
        if name_zav in i:
            return (i[0])
        
def poisk_for_name(r2:str):
    name_zav=r2
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM table_class')
    b=cur.fetchall()
    con.close()
    for i in b :
        if name_zav in i:
            return 'Yes'