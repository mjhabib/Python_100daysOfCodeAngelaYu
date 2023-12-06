student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}

for score in student_scores:
    scores = student_scores[score]
    if scores >= 91:
        student_grades[score] = "Outstanding"
    elif scores >= 81:
        student_grades[score] = "Exceeds Expectations"
    elif scores >= 71:
        student_grades[score] = "Acceptable"
    else:
        student_grades[score] = "Fail"

print(student_grades)
