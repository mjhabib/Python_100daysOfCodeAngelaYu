# FileNotFoundError
# with open("test_file.txt") as data:
#     data.read()

# KeyError
# test_dict = {"hey": 2}
# print(test_dict["nothing"])

# IndexError
# my_list = ["a", "b", "c"]
# print(my_list[3])

# TypeError
# text = "text"
# print(text + 5)

# try:  something that might cause an exception
# except:  do this if there was an exception
# else:  do this if there were no exception
# finally:  do this no matter what happens

try:
    a_file = open("a_test_file.txt")  # if the file does not exist
except:
    a_file = open("a_test_file.txt", "w")  # then create a new one
# do not use bare 'except' here, meaning if we add another causing error line of code there, it'll do nothing about it

# Ex:
try:
    b_file = open("b_test_file.txt")
    new_dict = {"key": "value"}
    print(new_dict["non_existence_key"])
except:
    b_file = open("b_test_file.txt", "w")
    # we won't get an error here even that we didn't catch the KeyError of "print", because the program considered the line of code above as a solution to our KeyError

# instead we should do this:
try:
    c_file = open("c_test_file.txt")
    new_dict = {"key": "value"}
    print(new_dict["non_existence_key"])
except FileNotFoundError:
    c_file = open("c_test_file.txt", "w")
    c_file.write("Something something")
    # now we get a KeyError because we specified our except to catch a specific error, i.e: FileNotFoundError
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist ...")
    # now we managed to catch all the errors
    # error_message is optional
else:  # if the file we're referring to doesn't exist, this line of code will not run
    content = c_file.read()
    print(content)
finally:
    a_file.close()
    b_file.close()
    c_file.close()
    print("\n" + "Execute this part no matter what!" + "\n")

# Raising your own Exceptions/Errors
height = float(input("Height: "))
weight = int(input("Weight: "))
bmi = weight / height ** 2

if height > 3:
    raise ValueError("\n" + "There is no human being taller than 3 meters!!!")

print(bmi)
