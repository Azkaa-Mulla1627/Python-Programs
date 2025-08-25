# Day 14
# Program to count vowels, consonants, digits, and special characters in a string using dictionary

def count_char_types(text):
    counts = {"vowels": 0, "consonants": 0, "digits": 0, "special": 0}
    vowels = "aeiouAEIOU"

    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                counts["vowels"] += 1
            else:
                counts["consonants"] += 1
        elif ch.isdigit():
            counts["digits"] += 1
        else:
            counts["special"] += 1

    return counts


# Example input
text = "Hello World! 123"
result = count_char_types(text)

# Display output
print("Character type counts:")
for k, v in result.items():
    print(f"{k} : {v}")
