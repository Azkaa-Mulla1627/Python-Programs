# Day 9
# Program 2 - Program to reverse each word in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()

reversed_words = [word[::-1] for word in words]
new_sentence = " ".join(reversed_words)

print("Sentence with each word reversed:", new_sentence)
