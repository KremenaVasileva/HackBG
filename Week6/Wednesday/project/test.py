import requests

user_url = "https://api.github.com/users/RadoRado?client_id=476883efbf9949576c17&client_secret=da89b579b746b7fb01bd3cc11980a45e64027fc4"
user_details = requests.get(user_url).json()
print(user_details['login'])
