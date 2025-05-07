import sqlite3


def get_connection():
    conn = None
    try:
        conn = sqlite3.connect('dados.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn