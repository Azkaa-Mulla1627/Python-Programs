# Day 15
# Program 1 - Program to print a right-aligned triangle pattern of stars

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
