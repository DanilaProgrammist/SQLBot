import sqlite3
import random
def build_bd():
    conn = sqlite3.connect("users.db")
    curs = conn.cursor()
    curs.execute("""create table if not exists users(
        name TEXT PRIMARY KEY,
        age INTEGER);
        
    """)
    conn.commit()
    print("База данных создана")


