# discuss about query optimization techniques used in mongodb
# explain aggregation operations used in mongodb

class User:
    def __init__(self, username, password):
       self.username = username
       self.password = password

    def login(self):
          if self.username == "Etiene" and self.password == "123":
              print("Login successfully")
          else:
           print("Login failed")

user = User("Etiene", "123")
user.login()