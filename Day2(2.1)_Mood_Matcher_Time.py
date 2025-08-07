# Day 2
# Program 1 : Mood Matcher Based on Time

hour = int(input("What hour is it (0–23)? "))

if 5 <= hour < 12:
    print("Good Morning! ☀️ Time for some tea?")
elif 12 <= hour < 17:
    print("Good Afternoon! 🍴 Hope your lunch was great!")
elif 17 <= hour < 21:
    print("Good Evening! 🌇 Time to relax.")
elif 21 <= hour <= 23 or 0 <= hour < 5:
    print("Good Night! 🌙 Don't forget to sleep well.")
else:
    print("Hmm... that's not a valid hour! 🤔")
