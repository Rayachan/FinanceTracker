import sqlite3 
import os
#using sqlite since it works within a container as long as it isnt reloaded

DATABASE= "expenses.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory= sqlite3.Row #helps return rows as dicts
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CRE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,,
        descrption TEXT,
        date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    #table is only created once when the app is first called 