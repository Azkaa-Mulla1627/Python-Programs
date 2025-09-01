# Day 16
# Program 2 : 
def reverse_string(s):
    # Base case
    if len(s) == 0:
        return s
    else:
        # Recursive step: reverse the substring excluding first char + first char
        return reverse_string(s[1:]) + s[0]

text = "github"
print("Original String:", text)
print("Reversed String:", reverse_string(text))
