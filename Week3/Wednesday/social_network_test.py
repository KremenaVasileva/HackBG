from panda_social_network import PandaSocialNetwork
from panda_social_network import Panda
from panda_social_network import PandaAlreadyThere
from panda_social_network import PandasAlreadyFriends
import unittest


class TestSocialPandaNetwork(unittest.TestCase):
    def setUp(self):
        self.network = PandaSocialNetwork()
        self.network.all_pandas = {}
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.pandio = Panda("Pandio", "pand@pand.pand", "male")
        self.hime = Panda("Hime", "hime@lala.com", "female")

    def test_init(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_add_panda(self):
        self.network.add_panda(self.ivo)
        self.assertTrue(self.ivo in self.network.all_pandas)

        with self.assertRaises(PandaAlreadyThere):
            self.network.add_panda(self.ivo)

    def test_has_panda(self):
        self.assertFalse(self.ivo in self.network.all_pandas)
        self.network.add_panda(self.ivo)
        self.assertTrue(self.ivo in self.network.all_pandas)

    def test_make_friends(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.pandio)
        self.network.make_friends(self.ivo, self.pandio)
        with self.assertRaises(PandasAlreadyFriends):
            self.network.make_friends(self.ivo, self.pandio)

    def test_are_friends(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.pandio)
        self.network.make_friends(self.ivo, self.pandio)
        self.assertTrue(self.network.are_friends(self.ivo, self.pandio))

    def test_friends_of(self):
        pass

    def test_connection_level_3_pandas(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        pandio = Panda("Pandio", "pand@pand.pand", "male")
        hime = Panda("Hime", "hime@lala.com", "female")
        self.network.add_panda(ivo)
        self.network.add_panda(pandio)
        self.network.add_panda(hime)
        self.network.make_friends(ivo, pandio)
        self.network.make_friends(pandio, hime)
        self.assertEqual(2, self.network.connection_level(ivo, hime))

    def test_are_connected(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.pandio)
        self.network.add_panda(self.hime)
        self.network.make_friends(self.ivo, self.pandio)
        self.assertTrue(self.network.are_connected(self.ivo, self.pandio))
        self.assertFalse(self.network.are_connected(self.ivo, self.hime))

    def test_gender_in_network(self):
        self.network.add_panda(self.ivo)
        self.network.add_panda(self.pandio)
        self.network.add_panda(self.hime)
        self.network.make_friends(self.ivo, self.pandio)
        self.network.make_friends(self.hime, self.pandio)
        result = self.network.how_many_gender_in_network(2, self.ivo, "female")
        self.assertEqual(1, result)


if __name__ == '__main__':
    unittest.main()
