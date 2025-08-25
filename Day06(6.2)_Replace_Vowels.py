# Day 6
# Program 2 -  Replace vowels in a string with the next alphabet character

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in text:
    if ch in vowels:
        result += chr(ord(ch) + 1)  # Replace with next alphabet
    else:
        result += ch

print("String after replacing vowels:", result)
