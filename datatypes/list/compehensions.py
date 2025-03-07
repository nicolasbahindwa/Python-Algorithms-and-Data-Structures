"""
List Comprehension Examples in Python
=====================================

This file contains examples demonstrating how list comprehensions work in Python,
from basic to more advanced usage patterns.

List comprehensions provide a concise way to create lists based on existing sequences.

Basic Syntax:
    new_list = [expression for item in iterable if condition]

    - expression: What to put in the new list
    - item: A variable representing each element in the iterable
    - iterable: The sequence you're iterating through
    - condition: (Optional) Only include items that meet this condition
"""

# Example 1: Basic list comprehension - Create a list of squares from 0-9
squares = [x**2 for x in range(10)]
print("1. Squares of numbers 0-9:")
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("\nThis is equivalent to:")
# The equivalent for-loop would be:
squares_loop = []
for x in range(10):
    squares_loop.append(x**2)
print(squares_loop)
print()

# Example 2: List comprehension with a condition - Get even numbers from 0-9
evens = [x for x in range(10) if x % 2 == 0]
print("2. Even numbers from 0-9:")
print(evens)  # Output: [0, 2, 4, 6, 8]
print("\nThis is equivalent to:")
# The equivalent for-loop would be:
evens_loop = []
for x in range(10):
    if x % 2 == 0:
        evens_loop.append(x)
print(evens_loop)
print()

# Example 3: Applying a function to each element
def double(x):
    return x * 2

doubled = [double(x) for x in range(5)]
print("3. Doubling each number from 0-4:")
print(doubled)  # Output: [0, 2, 4, 6, 8]
print()

# Example 4: Flattening a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print("4. Flattening a nested list:")
print(f"Original: {nested}")
print(f"Flattened: {flat}")  # Output: [1, 2, 3, 4, 5, 6]
print("\nThis is equivalent to:")
# The equivalent for-loops would be:
flat_loop = []
for sublist in nested:
    for item in sublist:
        flat_loop.append(item)
print(flat_loop)
print()

# Example 5: Creating a list of tuples (like a coordinate grid)
coordinates = [(x, y) for x in range(3) for y in range(2)]
print("5. Creating coordinates for a 3×2 grid:")
print(coordinates)  # Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
print("\nThis is equivalent to:")
# The equivalent for-loops would be:
coordinates_loop = []
for x in range(3):
    for y in range(2):
        coordinates_loop.append((x, y))
print(coordinates_loop)
print()

# Example 6: Filtering and transforming strings
words = ["hello", "world", "python", "programming"]
result = [word.upper() for word in words if len(word) > 5]
print("6. Upper-casing words longer than 5 characters:")
print(f"Original words: {words}")
print(f"Result: {result}")  # Output: ['PYTHON', 'PROGRAMMING']
print()

# Example 7: Working with dictionaries
prices = {"apple": 0.5, "banana": 0.25, "orange": 0.75, "pear": 0.60}
expensive = [fruit for fruit, price in prices.items() if price > 0.5]
print("7. Fruits costing more than $0.50:")
print(expensive)  # Output: ['orange', 'pear']
print()

# Example 8: Conditional expressions (if-else) in list comprehensions
numbers = [-5, -3, 0, 3, 5, 8]
result = [x if x > 0 else 0 for x in numbers]
print("8. Replace negative numbers with zero:")
print(f"Original: {numbers}")
print(f"Result: {result}")  # Output: [0, 0, 0
# 
# 
# Using a set comprehension instead of a list comprehension
word = "satoshinakamoto"
unique_chars = {char for char in word}
print("10. Unique characters in 'mississippi':")
print(unique_chars)  # Output: {'s', 'a', 't', 'o','h', 'i', 'n','k','m'}
print("Note that this is a set, not a list (no duplicates, unordered)")
print()

# Example 11: Dictionary comprehension
squares_dict = {x: x**2 for x in range(6)}
print("11. Creating a dictionary of squares:")
 