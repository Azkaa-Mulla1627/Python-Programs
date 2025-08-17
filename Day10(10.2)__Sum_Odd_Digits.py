# Day 10
# Program 2 - Find the sum of only odd digits in a given number

num = input("Enter a number: ")
total = 0

for digit in num:
    d = int(digit)
    if d % 2 != 0:   # odd digit
        total += d

print("Sum of odd digits:", total)
