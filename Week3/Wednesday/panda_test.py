from panda_social_network import Panda
import unittest


class TestPanda(unittest.TestCase):
    def setUp(self, name, email, male):
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.name = "Ivo"
        self.email = "ivo@pandamail.com"
        self.gender = "male"

    def test_init(self):
        self.assertTrue(isinstance(self.ivo, Panda))
        self.assertEqual(self.ivo.name, self.name)
        self.assertEqual(self.ivo.email, self.email)
        self.assertEqual(self.ivo.gender, self.gender)

        with self.assertRaises(ValueError):
            self.ivo = Panda("Ivo", "ivopandamail.com", "male")

    def test_gender(self):
        self.assertTrue(self.ivo.isMale())
        self.assertFalse(self.ivo.isFemale())

    def test_str(self):
        self.assertEqual(str(self.ivo), self.ivo.name)

    def test_eq(self):
        other_panda = Panda("Rado", "rado@lala.com", "male")
        self.assertFalse(self.ivo == other_panda)

    def test_hash(self):
        self.assertTrue(isinstance(self.ivo.__hash__(), int))

if __name__ == '__main__':
    unittest.main()
