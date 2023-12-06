class User:
    def __init__(self, name):
        self.name = name
        self.log_in = False


def log_in_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].log_in:  # == True
            function(args[0])

    return wrapper


@log_in_decorator
def create_blog_post(user):
    print(f"Welcome {user.name}")


new_user = User("MJ")
new_user.log_in = True
create_blog_post(new_user)  # Welcome MJ

another_user = User("Hasan")
another_user.log_in = False
create_blog_post(another_user)  # nothing should be appeared on screen
