# Day-9 
# Program 1 - Replace all even numbers in a list with their squares

numbers = [2, 5, 8, 3, 10, 7]
print("Original List:", numbers)

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = numbers[i] ** 2

print("Modified List:", numbers)
