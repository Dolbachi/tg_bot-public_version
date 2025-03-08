import sqlite3
from tkinter.font import names
from jinja2 import *
from test_class.classis import *
def get_name():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('SELECT name FROM table_class')
    names = [row[0] for row in cur.fetchall()]
    conn.close()
    return names
def get_adress():
    conn=sqlite3.connect('test.db')
    cur= conn.cursor()
    cur.execute('SELECT address from table_class')
    adress= [row[0].strip() for row in cur.fetchall()]
    conn.close()
    return adress


def get_name_from_class(cort:tuple):
    r2=Restaurant(id_table=cort[0],name=cort[1],address=cort[2],contact=cort[3],
                  working_hours=cort[4],delivery=cort[5],description=cort[6],
                  special=cort[7],rating=cort[8],feedback=cort[9])
    return r2


con=sqlite3.connect('test.db')
curs=con.cursor()
curs.execute('SELECT * FROM table_class')
c=curs.fetchall()
l=[]
for i in c:
    f=get_name_from_class(i)
    l.append(f)
con.commit()
con.close()


def create_shablon_html(l):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Cписок имен</title>
    </head>
    <body>
    <h1>Cписок имен</h1>
    <ul>
    """
    for name in l:
        html_content += f'           <li>{name}</li>\n'

    html_content +="""
    </ul>
    </body>
    </html>
    """
    return html_content


env=Environment(loader=FileSystemLoader(r'C:\Users\leham\Documents\GitHub\Kalmyk_info_bot-08\jinja2_sites\shablon1.html'))
shablon1=env.get_template('shablon1.html')
rend=shablon1.render(names=l)
f = open('shablon2.html','w', encoding='utf-8')
f.write(rend)