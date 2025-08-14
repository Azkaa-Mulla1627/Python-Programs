# Day 8
# Program 2 - Remove all duplicates from a list without using set()

numbers = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Original List:", numbers)
print("List without duplicates:", unique_list)
