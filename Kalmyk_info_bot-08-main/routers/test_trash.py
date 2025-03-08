import sqlite3
contact=sqlite3.connect('test.db')
cur=contact.cursor()
cur.execute('PRAGMA foreign_keys = ON;')
cur.execute('''CREATE TABLE IF NOT EXISTS Rating (
            id_rating INTEGER PRIMARY KEY,
            "1" INTEGER,
            "2" INTEGER,
            "3" INTEGER, 
            "4" INTEGER, 
            "5" INTEGER,
            id_table INTEGER,
            FOREIGN KEY (id_table) REFERENCES table_class(id_table) 
            ) ''')
contact.commit()
contact.close()