import sqlite3
from config.settings import DATABASE_NAME

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def check_connection():
    try:
        connection = get_connection()
        connection.close()
        return True
    except sqlite3.Error:
        return False