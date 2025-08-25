# Day 15
# Program 2 - Program to print a checkerboard pattern using stars

rows = 6
cols = 6

for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
