import re
from panda_bfs import bfs
import json


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class Panda():
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(
            self.name, self.email, self.gender)

    def __eq__(self, other):
        equal_names = self.name == other.name
        equal_emails = self.email == other.email
        equal_genders = self.gender == other.gender
        return equal_names and equal_emails and equal_genders

    def __hash__(self):
        return hash(self.get_email())

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def isMale(self):
        if self.gender == "male":
            return True
        else:
            return False

    def isFemale(self):
        if self.gender == "female":
            return True
        else:
            return False


class PandaSocialNetwork():
    def __init__(self):
        self.all_pandas = {}

    def getNetwork(self):
        return self.all_pandas

    def add_panda(self, new_panda):
        if new_panda in self.all_pandas:
            raise PandaAlreadyThere
        else:
            self.all_pandas[new_panda] = []

    def has_panda(self, panda):
        return panda in self.all_pandas

    def make_friends(self, panda, other_panda):
        if panda not in self.all_pandas:
            self.add_panda(panda)
        elif other_panda not in self.all_pandas:
            self.add_panda(other_panda)
        elif other_panda in self.all_pandas[panda]:
            raise PandasAlreadyFriends
        else:
            self.all_pandas[panda].append(other_panda)
            self.all_pandas[other_panda].append(panda)

    def are_friends(self, panda, other_panda):
        return other_panda in self.all_pandas[panda]

    def friends_of(self, panda):
        if panda not in self.all_pandas:
            return False
        else:
            return self.all_pandas[panda]

    def connection_level(self, first_panda, other_panda):
        if first_panda not in self.all_pandas:
            return False
        elif other_panda not in self.all_pandas:
            return False
        elif bfs(self.all_pandas, first_panda, other_panda) == 0:
            return -1
        return bfs(self.all_pandas, first_panda, other_panda)

    def are_connected(self, first_panda, second_panda):
        panda_connect_level = self.connection_level(first_panda, second_panda)
        if panda_connect_level in [-1, False]:
            return False
        else:
            return True

    def panda_level_histogram(self, original_panda):
        level_dict = {}
        for panda in self.all_pandas:
            level_dict[panda] = bfs(self.all_pandas, original_panda, panda)
        return level_dict

    def how_many_gender_in_network(self, level, panda, gender):
        level_dict = self.panda_level_histogram(panda)
        result = 0
        for panda in level_dict:
            if level_dict[panda] > 0 and level_dict[panda] <= level:
                if panda.gender == gender:
                    result += 1
        return result

    def json_repr(self):
        dict_repr = {}
        for panda in self.all_pandas:
            friend_list = [repr(panda_friend) for panda_friend in self.all_pandas[panda]]
            dict_repr[repr(panda)] = friend_list
        return json.dumps(dict_repr, indent="")

    def save(self, file_name):
        with open(file_name, "w") as myfile:
            myfile.write(self.json_repr())

    @staticmethod
    def load(file_name):
        loaded_network = PandaSocialNetwork()
        with open(file_name, "r") as myfile:
            db_contents = myfile.read()
            json_network = json.loads(db_contents)

        #print (json_network)

        for panda in json_network:
            friends = [eval(friend) for friend in json_network[panda]]
            panda = eval(panda)
            if not loaded_network.has_panda(panda):
                loaded_network.add_panda(panda)
                for panda_friend in friends:
                    if not loaded_network.are_friends(panda, panda_friend):
                        loaded_network.make_friends(panda, panda_friend)
        return loaded_network

ivo = Panda("Ivo", "ivo@pandamail.com", "male")
pandio = Panda("Pandio", "pand@pand.pand", "male")
hime = Panda("Hime", "hime@lala.com", "female")
network = PandaSocialNetwork()
network.add_panda(ivo)
network.add_panda(pandio)
network.add_panda(hime)
network.make_friends(ivo, pandio)
network.make_friends(pandio, hime)
network.save("SocialNetworkDatabase.txt")
print(network.how_many_gender_in_network(5, pandio, "female"))


test_network = PandaSocialNetwork()
test_network.load("SocialNetworkDatabase.txt")
print(test_network.are_connected(ivo, pandio))
print(network.getNetwork())