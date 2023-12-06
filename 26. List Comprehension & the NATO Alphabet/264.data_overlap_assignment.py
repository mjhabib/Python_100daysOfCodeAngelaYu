with open("file1.txt") as file1:
    file1_list = file1.readlines()

with open("file2.txt") as file2:
    file2_list = file2.readlines()


result = [int(x) for x in file1_list if x in file2_list]

print(result)
