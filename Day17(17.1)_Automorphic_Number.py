# Day 17
# Program 1 : rogram for Automorphic Number
def is_automorphic(num):
    square = num * num
    return str(square).endswith(str(num))

# Example usage
number = int(input("Enter a number: "))
if is_automorphic(number):
    print(number, "is an Automorphic number")
else:
    print(number, "is NOT an Automorphic number")
