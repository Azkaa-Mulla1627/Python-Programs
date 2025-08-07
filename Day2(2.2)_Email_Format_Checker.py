# Day 2
# Program 2 : Smart Email Format Verifier

email = input("Enter your email address: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("✅ This looks like a valid email format.")
else:
    print("❌ Invalid email format. Please check again.")
