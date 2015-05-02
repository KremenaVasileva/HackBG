from create_company import CreateDB


class IO:
    @staticmethod
    def init_database(database):
        database = CreateDB()
        database.add_employee("Ivan Ivanov", 5000, 10000,
                              "Software Developer")

        database.add_employee("Rado Rado", 500, 0,
                              "Technical Support Intern")

        database.add_employee("Ivo Ivo", 10000, 100000, "CEO")

        database.add_employee("Petar Petrov", 3000, 1000,
                              "Marketing Manager")

        database.add_employee("Maria Georgieva", 8000, 10000, "COO")

    @staticmethod
    def add_employee(database):
        try:
            name = input("name>")
            monthly_salary = input("monthly_salary>")
            yearly_bonus = input("yearly_bonus>")
            position = input("position>")
            database.add_employee(name, monthly_salary, yearly_bonus, position)
            print("New employee added!")
        except:
            print("Employee not added!")

    @staticmethod
    def list_employees(database):
        all_users = database.list_employees()

        for user in all_users:
            print("{} - {} - {}".format(user['id'],
                                        user['name'],
                                        user['position']))

    @staticmethod
    def monthly_spending(database):
        print (database.monthly_spending())

    @staticmethod
    def yearly_spending(database):
        print(database.yearly_spending())

    @staticmethod
    def delete_employee(database):
        try:
            employee_id = input("employee_id>")
            database.delete_employee(employee_id)
            print("Employee No.{} deleted!".format(employee_id))
        except:
            print("Employee not deleted!")

    @staticmethod
    def update_employee(database):
        try:
            employee_id = input("employee_id>")
            name = input("name>")
            monthly_salary = input("monthly_salary>")
            yearly_bonus = input("yearly_bonus>")
            position = input("position>")
            database.update_employee(employee_id, name, monthly_salary,
                                     yearly_bonus, position)
            print("Employee No.{} updated!".format(employee_id))
        except:
            print("Employee was not updated!")

    @staticmethod
    def execute_command(database, user_input):
        all_commands = {
                        "list": IO.list_employees,
                        "add": IO.add_employee,
                        "monthly_spending": IO.monthly_spending,
                        "yearly_spending": IO.yearly_spending,
                        "delete": IO.delete_employee,
                        "update": IO.update_employee
        }
        try:
            all_commands[user_input](database)
        except:
            print("Invalid command!")
