from create_company import CreateDB
from io_class import IO


def main():
    my_company = CreateDB()
    # my_company.initial_db()
    IO.init_database(my_company)
    user_input = input("command>")

    while True:
        IO.execute_command(my_company, user_input)
        user_input = input("command>")

if __name__ == '__main__':
    main()
