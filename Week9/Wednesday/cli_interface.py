from controller import Controller


class CLI:
    @staticmethod
    def register(database):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if Controller.register(database, username, password):
            print("Registration Successfull")

    @staticmethod
    def login(database):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        logged_user = Controller.login(database, username, password)

        if logged_user:
            CLI.logged_menu(database, logged_user)
        else:
            print("Login failed")

    @staticmethod
    def help(database):
        print("login - for logging in!")
        print("register - for creating new account!")
        print("exit - for closing program!")

    @staticmethod
    def logged_menu(db, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())

        while True:
            command = input("Logged>>")

            if command == 'info':
                user_info = Controller.logged_menu_info(db, logged_user)
                username = user_info['username']
                user_id = user_info['id']
                balance = user_info['balance']

                print("You are: " + str(username))
                print("Your id is: " + str(user_id))
                print("Your balance is:" + str(balance) + '$')

            elif command == 'changepass':
                new_pass = input("Enter your new password: ")
                Controller.logged_menu_changepass(db, new_pass, logged_user)
                print("Your password was changed successfully!")

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                Controller.logged_menu_change_message(db, new_message, logged_user)
                print("Your message was changed successfully!")

            elif command == 'show-message':
                print(Controller.logged_menu_show_message(db, logged_user))

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")

            elif command == 'exit':
                break

            else:
                print("Invalid command!")

    @staticmethod
    def execute_command(database, user_input):
        all_commands = {
                        "register": CLI.register,
                        "login": CLI.login,
                        "help": CLI.help,
        }
        all_commands[user_input](database)
