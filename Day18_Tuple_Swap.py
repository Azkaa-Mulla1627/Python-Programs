# Day 18
# Program : Swap two tuples without using a temporary variable

# Sample tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Before swapping:")
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

# Swapping using Python's tuple unpacking
tuple1, tuple2 = tuple2, tuple1

print("\nAfter swapping:")
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)
