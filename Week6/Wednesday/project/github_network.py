from directed_graph import DirectedGraph
from user import User


class GitHubNetwork:
    def __init__(self, user_url):
        self.user_url = user_url

        self.user_network = DirectedGraph()
        self.user = User(user_url)
        self.user.make_followers()
        self.user.make_following()

    def build_network(self, user_url, level):
        current_level = 0

        visited = set()
        visited.add(self.user)

        queue = []
        queue.append((current_level, self.user), )

        while len(queue) != 0:
            current_level, current_user = queue.pop(0)

            if current_level + 1 > level:
                break

            current_user.make_followers()
            current_user_followers = current_user.get_followers()

            current_user.make_following()
            current_user_following = current_user.get_following()

            for follower in current_user_followers:
                if follower not in visited:
                    self.user_network.add_edge(current_user, follower)
                    queue.append((current_level + 1, follower), )
                    visited.add(follower)

            for following in current_user_following:
                if following not in visited:
                    self.user_network.add_edge(following, current_user)
                    queue.append((current_level + 1, follower), )
                    visited.add(follower)

    def do_you_follow(self, user_followed):
        return self.user_network.edge_between(self.user, user_followed)

    def do_you_follow_indirectly(self, user_following):
        return self.user_network.path_between(self.user, user_following)

    def does_he_she_follows(self, user_following):
        self.user.make_following()
        if user_following.login in self.user.get_following():
            return True
        else:
            return False

    def does_he_she_follow_indirectly(self, user_following):
        return self.user_network.path_between(user_following, self.user)

person = User("https://api.github.com/users/KremenaVasileva?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4")
person.make_followers()
person.make_following()
person_network = GitHubNetwork("https://api.github.com/users/KremenaVasileva?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4")
person_network.build_network("https://api.github.com/users/KremenaVasileva?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4", 2)

new_user = User("https://api.github.com/users/6desislava6?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4")
new_user2 = User("https://api.github.com/users/radorado?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4")
# print(person_network.does_he_she_follows(new_user))
print(person_network.do_you_follow_indirectly(new_user))
