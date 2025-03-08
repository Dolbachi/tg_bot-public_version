import pandas
import openpyxl
from test_class.classis import Restaurant
import sqlite3

# Создаем объект класса Restaurant
r2 = Restaurant('106', "Balkan", "3", '4', '5', '6', '7', '8', '9', None)

# Получаем атрибуты и значения объекта
atr = list(r2.__dict__.keys())
val = list(r2.__dict__.values())
print(atr)

# Название таблицы
table_name = 'table_class'

# Создаем подключение к SQLite
con = sqlite3.connect('test.db')
curs = con.cursor()

# Создаем таблицу, если она не существует
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

# Вставляем данные в таблицу
curs.execute(
    f'INSERT INTO {table_name} ({", ".join([ atr[1], atr[2], atr[3], atr[4], atr[5], atr[6], atr[7], atr[8], atr[9]])}) VALUES (?,?,?,?,?,?,?,?,?)',
    ( val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8], val[9])
)

# Сохраняем изменения и закрываем соединение
con.commit()
con.close()


  