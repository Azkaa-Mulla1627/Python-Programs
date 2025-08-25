# Day 15
# Program 3 - Program to print a diamond pattern of stars

rows = 5

# Upper part
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)
