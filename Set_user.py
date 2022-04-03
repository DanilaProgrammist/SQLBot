import random
import sqlite3
def set_user(user):
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    age = random.randint(0,100)
    cursor.execute(f"INSERT or IGNORE INTO users VALUES (?,?)", (user, age))
    connect.commit()
    return "Пользователь добавлен"
