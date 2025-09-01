# Day-20
# Program: File Handling - Count lines, words, and characters in a file

def file_statistics(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

            # Count lines, words, and characters
            lines = content.split("\n")
            words = content.split()
            characters = len(content)

            print("File Statistics:")
            print(f"Total Lines: {len(lines)}")
            print(f"Total Words: {len(words)}")
            print(f"Total Characters: {characters}")

    except FileNotFoundError:
        print(f"The file {filename} does not exist. Please create it first.")

# Call the function with 'sample.txt'
file_statistics("sample1.txt")
