# Day 16
# Program 1 : Sum of digits using recursion  
def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0
    else:
        # Recursive step: last digit + sum of remaining digits
        return n % 10 + sum_of_digits(n // 10)

# Example usage
number = 12345
print("Number:", number)
print("Sum of digits:", sum_of_digits(number))
