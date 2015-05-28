import sqlite3
from Client import Client


class SQLManager:
    def __init__(self):
        self.conn = sqlite3.connect("bank.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

        create_query = """CREATE TABLE IF NOT EXISTS
            clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT,
                    balance REAL DEFAULT 0,
                    message TEXT)"""

        self.cursor.execute(create_query)

    def change_message(self, new_message, logged_user):
        update_sql = """UPDATE clients SET message = ? WHERE id = ?"""
        self.cursor.execute(update_sql, (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)

    def change_pass(self, new_pass, logged_user):
        update_sql = """UPDATE clients
                        SET password = ?
                        WHERE id = ?"""
        self.cursor.execute(update_sql, (new_pass, logged_user.get_id()))
        self.conn.commit()

    def register(self, username, password):
        insert_sql = """INSERT INTO clients (username, password)
                        VALUES (?, ?)"""
        self.cursor.execute(insert_sql, (username, password))
        self.conn.commit()

    def login(self, username, password):
        select_query = """SELECT id, username, balance, message
                          FROM clients
                          WHERE username = ? AND password = ?
                          LIMIT 1"""

        self.cursor.execute(select_query, (username, password))
        user = self.cursor.fetchone()

        if(user):
            return Client(user[0],  # id
                          user[1],  # username
                          user[2],  # balance
                          user[3])  # message
        else:
            return False
