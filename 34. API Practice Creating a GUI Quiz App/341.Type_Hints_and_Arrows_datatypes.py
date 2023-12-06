# we can associate a DataType with a variable but don't pass any values to do that later

number: int
name: str
pi: float
is_it: bool


# number = "text"  # error
number = 11


# Ex of a Type Hint:
def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive  # it expects a boolean as we specify it above


print(police_check(18))
# now that we want to pass something as a parameter, it expects an integer
