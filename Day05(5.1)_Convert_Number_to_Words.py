# Day 5
# Program 2 - Number to Words for 1–99

ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
         "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

num = int(input("Enter a number (1-99): "))

if num < 10:
    print("In words:", ones[num])
elif num < 20:
    print("In words:", teens[num - 10])
else:
    print("In words:", tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else ""))
