# Day 3
# Program 1 : Silent Mood Detector

time = int(input("What hour is it (0–23)? "))
place = input("Where are you right now? (home/office/class/public): ").lower()

if (22 <= time <= 23 or 0 <= time <= 7) or place in ['office', 'class', 'public']:
    print("🔇 Suggestion: Turn on Silent Mode.")
else:
    print("🔔 You’re good! No need for silent mode.")
