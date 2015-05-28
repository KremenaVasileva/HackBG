from directed_graph import DirectedGraph
import requests


class User:
    def __init__(self, user_url):
        user_details = requests.get(user_url).json()
        self.login = user_details['login']
        self.url = user_details['url']

        self.followers_url = "https://api.github.com/users/{}/followers?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4".format(self.login)
        self.following_url = "https://api.github.com/users/{}/following?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4".format(self.login)

        self.json_followers = requests.get(self.followers_url).json()
        self.json_following = requests.get(self.followers_url).json()

        self.followers = []
        self.following = []

#     def __repr__(self):
#         return self.url
# 
#     def __str__(self):
#        return self.url

    def make_followers(self):
        for follower in self.json_followers:
            follower_url = "https://api.github.com/users/{}?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4".format(follower['login'])
            user_follower = User(follower_url)
            if user_follower not in self.followers:
                self.followers.append(user_follower)

    def get_followers(self):
        return self.followers

    def make_following(self):
        for following in self.json_following:
            following_url = "https://api.github.com/users/{}?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4".format(following['login'])
            user_following = User(following_url)
            if user_following not in self.following:
                self.following.append(user_following)

    def get_following(self):
        return self.following


# user = User("https://api.github.com/users/KremenaVasileva?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4")
# user.make_followers()
# user.make_following()
# print(user.get_followers())
# print(user.login)
