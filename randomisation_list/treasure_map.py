'''
Treasure Map:
given a 3x3 grid ,
input column number,row number and update that coordinate with "X" to denote presence of treasure
'''

row1=["O","O","O"]
row2=["O","O","O"]
row3=["O","O","O"]
map=[row1,row2,row3]   #nested list,not related to map() of python..
print(f"{row1}\n{row2}\n{row3}") 

position=input("Where do you wish to put the treasure? ") #taking input as string

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")