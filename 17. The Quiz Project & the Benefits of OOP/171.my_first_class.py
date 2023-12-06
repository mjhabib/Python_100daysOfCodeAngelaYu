class User:
    # pass  # do nothing

    # this is how we construct our initializer:
    # every time we call our class, this initializer is going to be triggered
    # self is our actual initializer being created
    def __init__(self, user_id, username):  # usually, the name of parameters are ...
        self.id = user_id
        self.username = username  # ... equal to the name of attributes
        self.followers = 0  # this is a default amount we can associate it with our attribute
        self.following = 0

    def follow(self, user):  # this is how we create a method - self is for when we called our method via an object
        user.followers += 1  # user we're following
        self.following += 1  # self account following


# this is one way to make attributes:
# user1 = User()
# user1.id = "001"
# user1.username = "mjhabib"
# user1.color = "white"
#
# user2 = User()
# user2.id = "002"
# user2.name = "asdola"
# user2.family = "charkhi"

# instead of doing all these, we can initialize our attributes inside our class:
user1 = User("001", "mjhabib")
print(user1.id, user1.username)

user2 = User("002", "asdolacharkhi")
print(user2.id, user2.username)
print(user2.followers, "\n")

# calling our method:
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
