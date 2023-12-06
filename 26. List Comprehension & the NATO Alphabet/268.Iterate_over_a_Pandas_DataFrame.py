student_dict = {
    "student": ["MJ", "Hasan", "Naghi"],
    "score": [89, 75, 68],
}

# looping through a dict
for (key, value) in student_dict.items():
    print(key)  # student, score
    print(value)  # ['MJ', 'Hasan', 'Naghi'], [89, 75, 68]

# looping through a data frame
import pandas
student_data_frame = pandas.DataFrame(student_dict)
for (key, value) in student_data_frame.items():
    print(key)  # student, score
    print(value)
    # student
    # 0    MJ
    # 1    Hasan
    # 2    Naghi
    # Name: student, dtype: object
    # score
    # 0    89
    # 1    75
    # 2    68
    # Name: score, dtype: int64


# pandas inbuilt loop which is a method called 'iterrows'
for (index, row) in student_data_frame.iterrows():
    print(index)  # 0 1 2
    print(row)
    #     0
    # student    MJ
    # score      89
    # Name: 0, dtype: object
    # 1
    # student    Hasan
    # score         75
    # Name: 1, dtype: object
    # 2
    # student    Naghi
    # score         68
    print(row.score)  # [89, 75, 68]
    if row.student == "MJ":
        print(row.score)  # 89
