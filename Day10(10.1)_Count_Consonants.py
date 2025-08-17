# Day 10
# Program 1 - Count how many consonants are present in a string

text = input("Enter a string: ")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count = 0

for ch in text:
    if ch in consonants:
        count += 1

print("Number of consonants:", count)
