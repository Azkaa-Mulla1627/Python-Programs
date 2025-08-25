# Day 5
# Program 2 - Print numbers whose sum of digits is prime (within a range)

# Numbers whose sum of digits is prime

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

for num in range(start, end + 1):
    digit_sum = sum(int(d) for d in str(num))
    
    # Check if digit sum is prime
    if digit_sum > 1:
        for i in range(2, digit_sum):
            if digit_sum % i == 0:
                break
        else:
            print(num, end=" ")
