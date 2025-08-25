# Day 13
# Program 1 - Unique common elements between two lists (using sets)

# Input two lists from user
list1 = list(map(int, input("Enter numbers for first list (space separated): ").split()))
list2 = list(map(int, input("Enter numbers for second list (space separated): ").split()))

# Convert lists to sets and find unique common elements
common_elements = set(list1) & set(list2)

print("Unique common elements:", common_elements if common_elements else "No common elements found")
