# Day 7
# Program 1 - Extended Calculator: +, -, *, /, **, %, //

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Power (**)")
print("6. Modulus (%)")
print("7. Floor Division (//)")

choice = input("Enter choice (1-7): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero.")
elif choice == '5':
    print("Result:", num1 ** num2)
elif choice == '6':
    print("Result:", num1 % num2)
elif choice == '7':
    if num2 != 0:
        print("Result:", num1 // num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid choice!")
