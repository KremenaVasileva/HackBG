from Client import Client
from sql_manager import SQLManager


class Controller:
    @staticmethod
    def register(database, username, password):
        database.register(username, password)
        return True

    @staticmethod
    def login(database, username, password):
        return database.login(username, password)

    @staticmethod
    def logged_menu_info(database, logged_user):
        return {"username": logged_user.get_username(),
                "id": logged_user.get_id(),
                "balance": logged_user.get_balance()
                }

    @staticmethod
    def logged_menu_changepass(database, new_pass, logged_user):
        return database.change_pass(new_pass, logged_user)

    @staticmethod
    def logged_menu_change_message(database, new_message, logged_user):
        return database.change_message(new_message, logged_user)

    @staticmethod
    def logged_menu_show_message(database, logged_user):
        return logged_user.get_message()
