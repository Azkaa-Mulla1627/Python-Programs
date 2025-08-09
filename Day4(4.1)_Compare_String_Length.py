# Day 4
# Program 1 - Compare lengths of two strings and display result

# Taking input from the user
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Comparing lengths
if len(string1) > len(string2):
    print("First string is longer.")
elif len(string1) < len(string2):
    print("Second string is longer.")
else:
    print("Both strings have equal length.")
