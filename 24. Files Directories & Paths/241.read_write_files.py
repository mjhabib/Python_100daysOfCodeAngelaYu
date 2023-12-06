file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()  # to save computer's recourses

# another way to open a file without closing it because the codes are indented under it
with open("my_file.txt") as file2:
    contents2 = file2.read()
    print(contents2)

with open("my_file.txt", mode='a') as file3:  # default mode='r' == read-only
    # 'w' == write and replace all texts - 'a' == append to the previews texts
    file3.write("\nSomething, something new!")

new_file = open("new_file.txt", mode="w")
# it'll create a new file if it doesn't exist only in 'write' mode
new_file.write("New text ...")
# new_contents = new_file.read()
# print(new_contents)
new_file.close()

# for some reason I couldn't to write and read to a file at the same time, so I had to separate the codes in two parts

another_new_file = open("new_file.txt", mode="r")
new_contents = another_new_file.read()
print(new_contents)
another_new_file.close()

"""
because we're working in the same folder as our file exists,
we can access that file by a relative path like: "new_file.txt" or "./new_file.txt"
but if that file was in the parent folder: "../new_file.txt" == (pythonProject)
or even two parent folders back: "../../new_file.txt" == (Tools/pythonProject)

or these are our absolute paths:
"D:/Tools/new_files.txt"
"D:/Tools/pythonProject/new_files.txt"
"D:/Tools/pythonProject/24. Files Directories & Paths/new_files.txt"

Note: We replaced all backward-slashes '\' with forward-slashes '/'.
"""
