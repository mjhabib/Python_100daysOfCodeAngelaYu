print("Welcome to the Treasure Map game. Enjoy:) ")
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
t_map = [row1, row2, row3]
# t_map == [[a,b,c][e,f,g][h,i,j]] - From the computer perspective e = 01 (the first item from the second list) but the user will type 12, and I will turn it into 01 so the computer understand it (1-1, 2-1)
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Write a two didit number from 11 to 33? ")
column = position[0]
row = position[1]
int_column = int(column)
int_row = int(row)
# Now, since the user counts the ⬜️ from 1 but the program starts from 0, we have to make sure we don't get a 'list index out of range' error
if int_column != 0:
    int_column -= 1
if int_row != 0:
    int_row -= 1
t_map[int_row][int_column] = '😊'
print(f"{row1}\n{row2}\n{row3}")
