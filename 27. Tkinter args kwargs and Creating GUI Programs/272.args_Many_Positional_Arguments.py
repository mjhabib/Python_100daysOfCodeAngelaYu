# this is how we can put as many args as we want in a function

def add_nums(*args):  # I can name 'args' whatever I want
    add = 0
    for n in args:
        add += n
    print(add)  # 15
    print(args[4])  # 5 = since 'args' collect the numbers in a tuple, we can call any item inside by its index


add_nums(1, 2, 3, 4, 5)
