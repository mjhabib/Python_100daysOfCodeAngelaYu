student_scores = input("Type the scores and separate them with a space: ").split()
for x in range(len(student_scores)):
    student_scores[x] = int(student_scores[x])
highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print("The highest score: ", highest)

# another method
print("Max result: ", max(student_scores))
print("Min result: ", min(student_scores))
