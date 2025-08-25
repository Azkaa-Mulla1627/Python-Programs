# Day 3
# Program 2 : Color Emotion picker

color = input("Pick a color (red, blue, green, yellow, black, white): ").lower()

emotions = {
    "red": "🔴 Passion & Energy!",
    "blue": "🔵 Calm & Trust.",
    "green": "🟢 Growth & Balance.",
    "yellow": "🟡 Happiness & Positivity.",
    "black": "⚫ Elegance or Mystery.",
    "white": "⚪ Simplicity & Peace."
}

print(emotions.get(color, "🤔 That color’s emotion is unknown, but you're still awesome!"))
