"""
Python Tuples: A Comprehensive Guide with Time Complexity
--------------------------------------------------------

This document explains the various operations, use cases, and time complexities
of Python tuples with practical examples.
"""

# 1. Basic Tuple Creation and Access
print("\n--- 1. BASIC TUPLE OPERATIONS ---")

# Creating tuples - O(1) for initialization
empty_tuple = ()  # O(1)
single_element_tuple = (1,)  # O(1)
numbers_tuple = (1, 2, 3, 4, 5)  # O(5) = O(n) where n is the number of elements
mixed_tuple = (1, "hello", 3.14, True)  # O(4) = O(n)

print(f"Empty tuple: {empty_tuple}")
print(f"Single element tuple: {single_element_tuple}")
print(f"Numbers tuple: {numbers_tuple}")
print(f"Mixed tuple: {mixed_tuple}")

# Accessing elements by index - O(1) constant time
print(f"First element: {numbers_tuple[0]}")  # O(1)
print(f"Last element: {numbers_tuple[-1]}")  # O(1)
print(f"Slicing [1:3]: {numbers_tuple[1:3]}")  # O(k) where k is slice size

# 2. Tuple Modification
print("\n--- 2. TUPLE MODIFICATION ---")

# Tuples are immutable, so they cannot be modified in-place.
# We can, however, reassign a new tuple or modify it using concatenation.

# Reassigning a tuple (not modifying it in place) - O(n)
modified_tuple = numbers_tuple + (6, 7)  # O(n) for concatenation
print(f"After concatenation: {modified_tuple}")

# 3. Tuple Operations and Methods
print("\n--- 3. TUPLE OPERATIONS AND METHODS ---")

# Length of tuple - O(1) constant time
print(f"Length of numbers_tuple: {len(numbers_tuple)}")  # O(1)

# Count occurrences of an element - O(n)
count_of_2 = numbers_tuple.count(2)  # O(n)
print(f"Count of 2 in numbers_tuple: {count_of_2}")

# Find index of the first occurrence of an element - O(n)
index_of_4 = numbers_tuple.index(4)  # O(n)
print(f"Index of 4 in numbers_tuple: {index_of_4}")

# 4. Tuple Iteration
print("\n--- 4. ITERATING OVER TUPLES ---")

# Iterating over elements in a tuple - O(n)
for num in numbers_tuple:  # O(n) where n is the number of elements
    print(f"Element: {num}")

# 5. Nested Tuples
print("\n--- 5. NESTED TUPLES ---")

# Nested tuples - O(n*m) where n is the number of outer elements, m is the number of inner elements
nested_tuple = (1, (2, 3), (4, 5, 6), 7)

print(f"Nested tuple: {nested_tuple}")
for element in nested_tuple:  # O(n)
    print(f"Element: {element}")

# 6. Tuple Packing and Unpacking
print("\n--- 6. TUPLE PACKING AND UNPACKING ---")

# Packing values into a tuple - O(1)
packed_tuple = (1, "hello", 3.14)
print(f"Packed tuple: {packed_tuple}")

# Unpacking values from a tuple - O(1)
a, b, c = packed_tuple  # O(1)
print(f"Unpacked values: a = {a}, b = {b}, c = {c}")

# 7. Time Complexity of Tuple Operations
print("\n--- 7. TUPLE TIME COMPLEXITY ---")

# Accessing an element by index: O(1)
print(f"Accessing index 2 in tuple: {numbers_tuple[2]}")  # O(1)

# Concatenation (creating a new tuple): O(n + m) where n and m are the lengths of the tuples being concatenated
concat_tuple = numbers_tuple + (6, 7)  # O(n + m)
print(f"Concatenated tuple: {concat_tuple}")

# Counting occurrences: O(n)
print(f"Count of 2 in tuple: {numbers_tuple.count(2)}")  # O(n)

# Finding index: O(n)
print(f"Index of 4 in tuple: {numbers_tuple.index(4)}")  # O(n)

# 8. Tuple vs List
print("\n--- 8. TUPLE VS LIST ---")

# Lists are mutable, while tuples are immutable. This means tuples have certain advantages:
# - Tuples use less memory than lists (since they are immutable).
# - Tuples can be used as keys in dictionaries, while lists cannot.
# - Lists are more flexible, but tuples offer better performance for fixed data.

# Example of list vs tuple
numbers_list = [1, 2, 3]
numbers_tuple = (1, 2, 3)

# Accessing elements in a tuple vs list - O(1)
print(f"Accessing second element in list: {numbers_list[1]}")  # O(1)
print(f"Accessing second element in tuple: {numbers_tuple[1]}")  # O(1)

# 9. Time Complexity Summary
print("\n--- 9. TIME COMPLEXITY SUMMARY ---")
print("Operation               | Time Complexity")
print("------------------------|---------------")
print("Index access (t[i])     | O(1)")
print("Concatenation (t1 + t2) | O(n + m), where n and m are lengths of tuples")
print("Count (t.count(x))      | O(n)")
print("Index (t.index(x))      | O(n)")
print("Iteration (for x in t)  | O(n)")
print("Tuple packing           | O(1)")
print("Tuple unpacking         | O(1)")

print("\nThis guide covers the most common operations and use cases for Python tuples.")
