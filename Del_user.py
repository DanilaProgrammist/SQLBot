import sqlite3
def del_user(user):
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    try:
        sql_del = """DELETE FROM users WHERE name= ? """
        cursor.execute(sql_del, (user, ))
        return "Пользователь удалён"
    except sqlite3.Error as error:
        return "Такого пользователя нету😫"
    finally:
        connect.commit()
