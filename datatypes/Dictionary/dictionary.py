"""
Python Dictionaries: A Comprehensive Guide with Time Complexity
-------------------------------------------------------------

This document explains the various operations, use cases, and time complexities
of Python dictionaries with practical examples.
"""

# 1. Basic Dictionary Creation and Access
print("\n--- 1. BASIC DICTIONARY OPERATIONS ---")

# Creating dictionaries - O(1) for initialization
empty_dict = {}  # O(1)
person = {"name": "Alice", "age": 25, "city": "New York"}  # O(3) = O(n) where n is the number of keys

print(f"Empty dictionary: {empty_dict}")
print(f"Person dictionary: {person}")

# Accessing elements by key - O(1) average time complexity
print(f"Name: {person['name']}")   # O(1)
print(f"Age: {person['age']}")     # O(1)
print(f"City: {person['city']}")   # O(1)

# 2. Dictionary Modification
print("\n--- 2. DICTIONARY MODIFICATION ---")

# Adding or updating elements - O(1) average time complexity
person["email"] = "alice@example.com"  # O(1)
person["age"] = 26  # O(1)
print(f"Updated person dictionary: {person}")

# Removing elements - O(1) average time complexity
del person["email"]  # O(1)
print(f"After removing 'email': {person}")

# Using pop() method - O(1) average time complexity
removed_item = person.pop("age")  # O(1)
print(f"Removed item: {removed_item}")
print(f"After pop('age'): {person}")

# 3. Dictionary Operations and Methods
print("\n--- 3. DICTIONARY OPERATIONS AND METHODS ---")

# Length of dictionary - O(1) constant time
print(f"Length of person dictionary: {len(person)}")  # O(1)

# Checking for key existence - O(1) average time complexity
print(f"Is 'city' a key in dictionary?: {'yes' if 'city' in person else 'no'}")  # O(1)
print(f"Is 'email' a key in dictionary?: {'yes' if 'email' in person else 'no'}")  # O(1)

# Get method - O(1) average time complexity
city = person.get("city", "Not Found")  # O(1)
print(f"City: {city}")

# Dictionary keys, values, and items - O(n) where n is the number of key-value pairs
keys = person.keys()   # O(n)
values = person.values()  # O(n)
items = person.items()  # O(n)
print(f"Keys: {keys}, Values: {values}, Items: {items}")

# 4. Iterating Over a Dictionary
print("\n--- 4. ITERATING OVER DICTIONARY ---")

# Iterating over keys - O(n)
for key in person:  # O(n) where n is the number of keys
    print(f"Key: {key}, Value: {person[key]}")

# Iterating over values - O(n)
for value in person.values():  # O(n)
    print(f"Value: {value}")

# Iterating over items (key-value pairs) - O(n)
for key, value in person.items():  # O(n)
    print(f"{key}: {value}")

# 5. Nested Dictionaries (Dictionaries of Dictionaries)
print("\n--- 5. NESTED DICTIONARIES ---")

# Nested dictionary - O(n*m) where n is number of outer keys and m is average number of inner keys
students = {
    "Alice": {"age": 22, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"},
    "Charlie": {"age": 23, "grade": "A-"}
}

print("Students dictionary:")
for student, details in students.items():  # O(n) where n is number of outer keys
    print(f"{student} -> Age: {details['age']}, Grade: {details['grade']}")

# 6. Dictionary Comprehensions
print("\n--- 6. DICTIONARY COMPREHENSIONS ---")

# Create a dictionary of squares - O(n)
squares_dict = {x: x**2 for x in range(1, 6)}  # O(n)
print(f"Squares dictionary: {squares_dict}")

# Filtering with dictionary comprehension - O(n)
filtered_dict = {key: value for key, value in squares_dict.items() if value > 10}  # O(n)
print(f"Filtered dictionary (values > 10): {filtered_dict}")

# 7. Merging Dictionaries
print("\n--- 7. MERGING DICTIONARIES ---")

# Merging two dictionaries - O(n + m) where n and m are sizes of the dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}  # O(n + m)
print(f"Merged dictionary: {merged_dict}")

# Using update() method - O(m) where m is the size of the dictionary being added
dict1.update(dict2)  # O(m)
print(f"After update() on dict1: {dict1}")

# 8. Time Complexity of Common Dictionary Operations
print("\n--- 8. DICTIONARY TIME COMPLEXITY ---")

# Inserting a new key-value pair or updating an existing one: O(1)
person["email"] = "alice@example.com"  # O(1)

# Deleting a key-value pair: O(1) average time
del person["email"]  # O(1)

# Checking if a key exists: O(1) average time
print(f"Is 'email' in dictionary?: {'yes' if 'email' in person else 'no'}")  # O(1)

# Getting a value for a key: O(1) average time
email = person.get("email", "Not Found")  # O(1)
print(f"Email: {email}")

# Iterating over keys, values, or items: O(n)
for key in person:  # O(n)
    print(f"Key: {key}, Value: {person[key]}")

# 9. Dictionary vs Lists
print("\n--- 9. DICTIONARY VS LISTS ---")

# Lists - O(1) for accessing by index, but slower for searching (O(n))
# Dictionaries - O(1) for accessing by key, faster for searches by key

# Example of list vs dictionary for accessing elements
names_list = ["Alice", "Bob", "Charlie"]
names_dict = {"Alice": 0, "Bob": 1, "Charlie": 2}

# Accessing by index in list - O(1)
print(f"Accessing index 1 in list: {names_list[1]}")  # O(1)

# Accessing by key in dictionary - O(1)
print(f"Accessing 'Bob' in dictionary: {names_dict['Bob']}")  # O(1)

# 10. Time Complexity Summary
print("\n--- 10. TIME COMPLEXITY SUMMARY ---")
print("Operation               | Time Complexity")
print("------------------------|---------------")
print("Insert or Update (dict[key] = value) | O(1)")
print("Delete (del dict[key])  | O(1) average time")
print("Get (dict.get(key))      | O(1) average time")
print("Check key existence (key in dict) | O(1)")
print("Iterate over keys (for key in dict) | O(n)")
print("Iterate over values (for value in dict.values()) | O(n)")
print("Iterate over items (for key, value in dict.items()) | O(n)")
print("Merge (dict1.update(dict2)) | O(m), where m is size of dict2")
print("Dictionary comprehension | O(n)")

print("\nThis guide covers the most common operations and use cases for Python dictionaries.")
