# Day 11
# Program 1 - Count Vowels in a String using Function

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

sentence = "Python programming is fun"
print("Sentence:", sentence)
print("Number of vowels:", count_vowels(sentence))
