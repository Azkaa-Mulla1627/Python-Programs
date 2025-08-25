# Day 9
# Program 1 - Program to count how many words in a sentence start and end with the same letter

sentence = input("Enter a sentence: ").lower()
words = sentence.split()

count = 0
for word in words:
    if len(word) > 1 and word[0] == word[-1]:
        count += 1

print("Number of words starting and ending with the same letter:", count)
