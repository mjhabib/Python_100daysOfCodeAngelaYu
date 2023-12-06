# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# items() == Returns the dictionary's key-value pairs

import random

names = ["MJ", "Hasan", "Kojoy", "Naboodi", "Nisti", "KamPeyday", "Hehe"]

# creating a new dict
students_scores = {student: random.randint(50, 100) for student in names}
print(students_scores)

# printing students who have a score above 70
passed_students = {student: score for (student, score) in students_scores.items() if score > 70}
print(passed_students)
