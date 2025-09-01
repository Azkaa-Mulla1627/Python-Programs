# Day 19
# Program : To count word frequency in a text file

def word_frequency(sample):
    freq = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower().strip(".,!?")
                    freq[word] = freq.get(word, 0) + 1

        print("Word Frequency in file:")
        for word, count in freq.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found. Please check the filename.")

# Example usage:
# First create a file named "sample.txt" with some text inside
word_frequency("sample.txt")
