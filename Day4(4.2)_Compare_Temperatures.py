# Day 4
# Program 2: Compare two temperatures and display which is higher

# Taking temperature inputs
temp_city1 = float(input("Enter temperature of City 1 (in °C): "))
temp_city2 = float(input("Enter temperature of City 2 (in °C): "))

# Comparing temperatures
if temp_city1 > temp_city2:
    print("City 1 is hotter.")
elif temp_city1 < temp_city2:
    print("City 2 is hotter.")
else:
    print("Both cities have the same temperature.")
