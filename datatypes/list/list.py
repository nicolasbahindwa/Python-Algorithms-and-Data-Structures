"""
Python Lists: A Comprehensive Guide with Time Complexity
-------------------------------------------------------

This document explains the various operations, use cases, and time complexities
of Python lists with practical examples.
"""

# 1. Basic List Creation and Access
print("\n--- 1. BASIC LIST OPERATIONS ---")

# Creating lists - O(n) where n is the number of elements
empty_list = []                     # O(1)
numbers = [1, 2, 3, 4, 5]           # O(5) = O(n)
mixed_list = [1, "hello", 3.14, True]  # O(4) = O(n)

print(f"Empty list: {empty_list}")
print(f"Number list: {numbers}")
print(f"Mixed list: {mixed_list}")

# Accessing elements - O(1) constant time
print(f"First element: {numbers[0]}")     # O(1)
print(f"Last element: {numbers[-1]}")     # O(1)
print(f"Slicing [1:3]: {numbers[1:3]}")   # O(k) where k is the slice size

# 2. List Modification
print("\n--- 2. LIST MODIFICATION ---")

# Adding elements
numbers.append(6)  # O(1) - Amortized constant time
print(f"After append(6): {numbers}")

numbers.insert(2, 2.5)  # O(n) - Linear time (shifts elements)
print(f"After insert(2, 2.5): {numbers}")

numbers.extend([7, 8, 9])  # O(k) where k is length of list being added
print(f"After extend([7, 8, 9]): {numbers}")

# Removing elements
popped_value = numbers.pop()  # O(1) - Constant time for last element
print(f"Popped value: {popped_value}")
print(f"After pop(): {numbers}")

popped_index = numbers.pop(2)  # O(n) - Linear time (shifts elements)
print(f"Popped at index 2: {popped_index}")
print(f"After pop(2): {numbers}")

numbers.remove(7)  # O(n) - Linear time (searches then shifts)
print(f"After remove(7): {numbers}")

# Clearing a list
numbers_copy = numbers.copy()  # O(n) - Linear time to copy all elements
numbers_copy.clear()  # O(1) - Constant time
print(f"After clear(): {numbers_copy}")

# 3. List Operations and Methods
print("\n--- 3. LIST OPERATIONS AND METHODS ---")

# Length of list
print(f"Length of numbers: {len(numbers)}")  # O(1) - Constant time

# Check if item exists
print(f"Is 4 in list?: {'yes' if 4 in numbers else 'no'}")  # O(n) - Linear search
print(f"Is 10 in list?: {'yes' if 10 in numbers else 'no'}")  # O(n) - Linear search

# Count occurrences
new_list = [1, 2, 2, 3, 2, 4, 5, 2]
print(f"Count of 2 in {new_list}: {new_list.count(2)}")  # O(n) - Linear scan

# Find index of first occurrence
print(f"Index of 3 in {new_list}: {new_list.index(3)}")  # O(n) - Linear search

# Sorting and reversing
sorted_list = sorted(new_list)  # O(n log n) - Timsort algorithm
print(f"Sorted list (new): {sorted_list}")

new_list.sort()  # O(n log n) - Timsort algorithm in-place
print(f"Sorted list (in-place): {new_list}")

new_list.reverse()  # O(n) - Linear time
print(f"Reversed list: {new_list}")

# List comprehensions
squares = [x**2 for x in range(1, 6)]  # O(n) - Linear time
print(f"Squares 1-5: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]  # O(n) - Linear time
print(f"Even squares 1-10: {even_squares}")

# 4. Multi-dimensional Lists (2D Arrays)
print("\n--- 4. MULTI-DIMENSIONAL LISTS ---")

# 2D list/matrix - O(n*m) for creation where n is rows, m is columns
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:  # O(n*m) where n is rows, m is columns
    print(row)

# Accessing elements in 2D list - O(1)
print(f"Matrix[1][2]: {matrix[1][2]}")  # O(1) - Constant time

# Create a 3x3 matrix of zeros using list comprehension - O(n*m)
zeros = [[0 for _ in range(3)] for _ in range(3)]  # O(3*3) = O(n*m)
print("3x3 Matrix of zeros:")
for row in zeros:
    print(row)

# 5. Lists of Dictionaries (Common for Data Processing)
print("\n--- 5. LISTS OF DICTIONARIES ---")

students = [
    {"name": "Alice", "age": 22, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 23, "grade": "A-"}
]  # O(n) where n is number of dictionaries

print("Students list:")
for student in students:  # O(n) where n is length of list
    # Dictionary key access is O(1)
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# Filtering with list comprehension - O(n)
a_students = [s for s in students if s["grade"].startswith("A")]  # O(n)
print(f"Students with A grades: {a_students}")

# 6. Advanced List Operations
print("\n--- 6. ADVANCED LIST OPERATIONS ---")

# Flattening a nested list using list comprehension
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# O(n) where n is total number of elements across all sublists
flattened = [num for sublist in nested_list for num in sublist]
print(f"Flattened list: {flattened}")

# Using zip to work with multiple lists simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "Boston", "Chicago"]

# O(n) where n is length of shortest list
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# 7. Comparing Lists with Arrays
print("\n--- 7. LISTS VS ARRAYS ---")

import array

# Regular list - can contain any data type - O(n) to create
regular_list = [1, 2, 3, 4, 5]

# Arrays - must contain elements of the same type - O(n) to create
# 'i' represents signed integers
int_array = array.array('i', [1, 2, 3, 4, 5])

print(f"Regular list: {regular_list}")
print(f"Integer array: {int_array}")
print("Lists are more flexible but arrays are more memory-efficient for numerical data")

# 8. Memory Considerations
print("\n--- 8. MEMORY CONSIDERATIONS ---")

import sys

integer_list = [1, 2, 3, 4, 5]
integer_array = array.array('i', [1, 2, 3, 4, 5])

print(f"Memory size of list: {sys.getsizeof(integer_list)} bytes")
print(f"Memory size of array: {sys.getsizeof(integer_array)} bytes")
print("Arrays typically use less memory than lists for the same numerical data")

# 9. Common Pitfalls and Tips
print("\n--- 9. COMMON PITFALLS AND TIPS ---")

# Modifying a list while iterating (using a slice copy)
original = [1, 2, 3, 4, 5]
print(f"Original list: {original}")

# Incorrect way (modifies list during iteration)
# Uncommenting this will show the issue:
# for item in original:
#     if item == 3:
#         original.remove(item)  # O(n) operation during iteration - problematic!

# Correct way: iterate over a copy
for item in original[:]:  # Using slice creates a copy - O(n)
    if item == 3:
        original.remove(item)  # O(n) but safe because we're iterating over a copy

print(f"After removing 3: {original}")

# Creating copies vs references
list1 = [1, 2, 3]
list2 = list1  # O(1) - This creates a reference, not a copy!

list2.append(4)  # O(1)
print(f"list1 after modifying list2: {list1}")  # list1 is also modified

# Proper copying
list3 = [1, 2, 3]
list4 = list3.copy()  # O(n) - Creates a true copy
# Alternative ways: list4 = list(list3) or list4 = list3[:]

list4.append(4)  # O(1)
print(f"list3 after modifying list4: {list3}")  # list3 remains unchanged
print(f"list4 after modification: {list4}")

# 10. Time Complexity Summary
print("\n--- 10. TIME COMPLEXITY SUMMARY ---")
print("Operation               | Time Complexity")
print("------------------------|---------------")
print("Index access (l[i])     | O(1)")
print("Append (l.append(x))    | O(1) amortized")
print("Pop from end (l.pop())  | O(1)")
print("Pop from index (l.pop(i))| O(n)")
print("Insert (l.insert(i, x)) | O(n)")
print("Remove (l.remove(x))    | O(n)")
print("Extend (l.extend(l2))   | O(k) - k is len(l2)")
print("Check membership (x in l)| O(n)")
print("Copy (l.copy(), l[:])   | O(n)")
print("Length (len(l))         | O(1)")
print("Sort (l.sort())         | O(n log n)")
print("Slice (l[a:b])          | O(b-a)")
print("Min/Max (min(l), max(l))| O(n)")
print("Reverse (l.reverse())   | O(n)")
print("Iteration (for x in l)  | O(n)")
print("List comprehension      | O(n)")

print("\nThis guide covers the most common operations and use cases for Python lists.")