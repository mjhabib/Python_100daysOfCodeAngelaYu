# first we need to make a list and use the for loop to turn this string list to integer
student_heights = input("Type the heights and separate them with a space: ").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])
# now we need to add all the heights using a for loop function
total_height = 0
for height in student_heights:
    total_height += height
# to calculate the average height, we need to know the number of students
num_students = 0
for student in student_heights:
    num_students += 1
# finally a simple math
print("Result: ", round(total_height / num_students))

# solution #2
# counter = 0
# total = 0
# for x in range(0, len(student_heights)):
#     student_heights[x] = int(student_heights[x])
#     total += student_heights[x]
#     counter += 1
# print("Sum of all elements in given list: ", round(total / counter))

# Solution #3
# for average in range(0, len(student_heights)):
    # student_heights[average] = int(student_heights[average])
# add = sum(student_heights)
# total = add / len(student_heights)
# print(round(total))
