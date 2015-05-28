from database import CreateDB
from io_class import IO


def main():
    hack_database = CreateDB()
    IO.init_database(hack_database)
    user_input = input("command>")

    while True:
        IO.execute_command(hack_database, user_input)
        user_input = input("command>")


if __name__ == '__main__':
    main()
