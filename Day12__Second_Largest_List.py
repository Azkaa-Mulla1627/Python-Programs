 # Day 12
# Program 1 - Find Second Largest Element in a List Without Using max()

numbers = [12, 45, 2, 67, 33, 67, 45]

first, second = float("-inf"), float("-inf")
for num in numbers:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print("List:", numbers)
print("Second Largest Element:", second)
