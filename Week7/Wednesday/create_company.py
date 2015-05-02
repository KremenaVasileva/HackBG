import sqlite3


class CreateDB:
    def __init__(self):
        self.db = sqlite3.connect('company')
        # gets the response of the query in dict format
        # instead of a list
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS company(
            id INTEGER PRIMARY KEY,
            name TEXT,
            monthly_salary INTEGER,
            yearly_bonus INTEGER,
            position TEXT) """)

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute("""INSERT INTO company(
            name, monthly_salary, yearly_bonus, position)
            VALUES(?, ?, ?, ?)
            """, (name, monthly_salary, yearly_bonus, position))
        self.db.commit()

    def list_employees(self):
        return self.cursor.execute("""SELECT id, name, position
            FROM company
            """)

    def monthly_spending(self):
        self.cursor.execute("""SELECT monthly_salary
            FROM company
            """)
        employee_salaries = self.cursor.fetchall()

        monthly_spending = 0

        for salary in employee_salaries:
            monthly_spending += salary['monthly_salary']

        return monthly_spending

    def yearly_spending(self):
        yearly_spending = self.monthly_spending()

        self.cursor.execute("""SELECT yearly_bonus
            FROM company
            """)
        employee_bonuses = self.cursor.fetchall()

        for bonus in employee_bonuses:
            yearly_spending += bonus['yearly_bonus']

        return yearly_spending

    def delete_employee(self, employee_id):
        self.cursor.execute("""DELETE FROM company
            WHERE id = (?)
            """, (employee_id, ))
        self.db.commit()

    def update_employee(self, employee_id, name, monthly_salary, yearly_bonus, position):
        self.cursor.execute("""UPDATE company
            SET name = ?, monthly_salary = ?, yearly_bonus = ?, position = ?
            WHERE id = ?
            """, (name, monthly_salary, yearly_bonus, position, employee_id))
