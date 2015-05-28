from sql_manager import SQLManager
from cli_interface import CLI


def main():
    print("Welcome to our bank service. You are not logged in.")
    print("Please register or login")

    my_db = SQLManager()
    while True:
        command = input("$$$>")
        if command == 'exit':
            break
        CLI.execute_command(my_db, command)

    # with open(DB_STR, "r") as f:
    #     cursor.executescript(f.read())

if __name__ == '__main__':
    main()
