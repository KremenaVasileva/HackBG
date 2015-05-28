class Student:
    def __init__(self, github, name):
        self.name = name
        self.github = github

    def __repr__(self):
        return self.name
