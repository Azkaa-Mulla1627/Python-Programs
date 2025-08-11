# Day 6
# Program 1 - Count how many words in a sentence are palindromes

sentence = input("Enter a sentence: ").lower()
words = sentence.split()
count = 0

for word in words:
    if word == word[::-1]:
        count += 1

print(f"Number of palindromic words: {count}")
