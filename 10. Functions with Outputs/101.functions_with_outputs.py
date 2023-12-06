def format_name(f_name, l_name):
    """Take a first and last name and format it in a title-cased string."""
    # The line above is called 'docstring' which is going to guide us during calling the function

    if f_name == '' or l_name == '':
        return  # return 'none' and won't go through other lines of code
        # return "You didn't type anything!"

    formated_first_name = f_name.title()  # returns a title-cased string
    formated_last_name = l_name.title()
    return f"{formated_first_name} {formated_last_name}"
    # return formated_first_name, formated_last_name - creates a list
    # note: return is the end of our function and any line of code after that, won't work!


print(format_name(input("Type your name: "), input("Type your family name: ")))
# long version:
# formated_string = format_name(input("Type your name: "), input("Type your family name: "))
# print(formated_string)

