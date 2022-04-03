import sqlite3
def find_user(user):
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    sql_find = """SELECT age from users where name = ? """
    try:
        cursor.execute(sql_find, (user,))
        data = cursor.fetchall()
        for answer in data:
            return answer[0]
    except sqlite3.Error as error:
        return "Такого пользователя нету😫"
    finally:
        connect.commit()

