import sys
import unittest
import os

sys.path.append("..")
from sql_manager import SQLManager


class SqlManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = SQLManager()
        self.manager.register('Tester', '123')

    def tearDown(self):
        self.manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_register(self):
        self.manager.register('Dinko', '123123')

        self.manager.cursor.execute("""SELECT Count(*)
                                      FROM clients
                                      WHERE username = (?)
                                      AND password = (?)""",
                                    ('Dinko', '123123'))
        users_count = self.manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = self.manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = self.manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = self.manager.login('Tester', '123')
        new_message = "podaivinototam"
        self.manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = self.manager.login('Tester', '123')
        new_password = "12345"
        self.manager.change_pass(new_password, logged_user)

        logged_user_new_password = self.manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
