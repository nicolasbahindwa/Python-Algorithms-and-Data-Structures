"""
Python Sets: A Comprehensive Guide with Time Complexity
------------------------------------------------------

This document explains the various operations, use cases, and time complexities
of Python sets with practical examples.
"""

# 1. Basic Set Creation and Access
print("\n--- 1. BASIC SET OPERATIONS ---")

# Creating sets - O(1) for initialization
empty_set = set()  # O(1)
numbers_set = {1, 2, 3, 4, 5}  # O(n) where n is the number of elements
mixed_set = {1, "hello", 3.14, True}  # O(n) where n is the number of elements

print(f"Empty set: {empty_set}")
print(f"Numbers set: {numbers_set}")
print(f"Mixed set: {mixed_set}")

# Sets do not allow duplicate values; duplicates are automatically removed
duplicate_set = {1, 2, 3, 3, 2, 1}  # O(n)
print(f"Set with duplicates (duplicates removed): {duplicate_set}")

# 2. Set Operations
print("\n--- 2. SET OPERATIONS ---")

# Adding elements - O(1) average case for add
numbers_set.add(6)  # O(1) - average case
print(f"After add(6): {numbers_set}")

# Removing elements - O(1) average case for discard and remove
numbers_set.discard(3)  # O(1)
print(f"After discard(3): {numbers_set}")

# Removing an element (raises KeyError if element not found) - O(1)
numbers_set.remove(4)  # O(1)
print(f"After remove(4): {numbers_set}")

# Pop an arbitrary element - O(1)
popped_value = numbers_set.pop()  # O(1)
print(f"Popped value: {popped_value}")
print(f"After pop(): {numbers_set}")

# Clearing a set - O(n) to remove all elements
numbers_set.clear()  # O(n)
print(f"After clear(): {numbers_set}")

# 3. Set Operations (Union, Intersection, Difference)
print("\n--- 3. SET OPERATIONS (UNION, INTERSECTION, DIFFERENCE) ---")

# Union - O(n + m) where n and m are the lengths of the sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)  # O(n + m)
print(f"Union of set_a and set_b: {union_set}")

# Intersection - O(min(n, m)) where n and m are the lengths of the sets
intersection_set = set_a.intersection(set_b)  # O(min(n, m))
print(f"Intersection of set_a and set_b: {intersection_set}")

# Difference - O(n) where n is the length of the first set
difference_set = set_a.difference(set_b)  # O(n)
print(f"Difference of set_a and set_b: {difference_set}")

# Symmetric Difference - O(n + m)
symmetric_difference_set = set_a.symmetric_difference(set_b)  # O(n + m)
print(f"Symmetric difference of set_a and set_b: {symmetric_difference_set}")

# 4. Set Membership Test
print("\n--- 4. SET MEMBERSHIP TEST ---")

# Checking membership - O(1) average case
print(f"Is 3 in set_a?: {'yes' if 3 in set_a else 'no'}")  # O(1)
print(f"Is 6 in set_a?: {'yes' if 6 in set_a else 'no'}")  # O(1)

# 5. Set Iteration
print("\n--- 5. ITERATING OVER SETS ---")

# Iterating over elements in a set - O(n)
for element in set_a:  # O(n)
    print(f"Element: {element}")

# 6. Set Comprehensions
print("\n--- 6. SET COMPREHENSIONS ---")

# Creating a set of squares - O(n)
squares_set = {x**2 for x in range(1, 6)}  # O(n)
print(f"Squares set: {squares_set}")

# Creating a set with condition - O(n)
even_squares_set = {x**2 for x in range(1, 11) if x % 2 == 0}  # O(n)
print(f"Even squares set: {even_squares_set}")

# 7. Time Complexity of Set Operations
print("\n--- 7. SET TIME COMPLEXITY ---")

# Accessing elements and membership tests: O(1) average case
print(f"Is 3 in numbers_set?: {'yes' if 3 in numbers_set else 'no'}")  # O(1)

# Union: O(n + m)
union_set = set_a | set_b  # O(n + m)
print(f"Union (using |): {union_set}")

# Intersection: O(min(n, m))
intersection_set = set_a & set_b  # O(min(n, m))
print(f"Intersection (using &): {intersection_set}")

# Difference: O(n)
difference_set = set_a - set_b  # O(n)
print(f"Difference (using -): {difference_set}")

# Symmetric Difference: O(n + m)
symmetric_difference_set = set_a ^ set_b  # O(n + m)
print(f"Symmetric difference (using ^): {symmetric_difference_set}")

# 8. Set vs List
print("\n--- 8. SETS VS LISTS ---")

# Sets:
# - Cannot contain duplicate elements
# - Do not maintain order
# - Provide faster membership testing (O(1) on average)
# - Use hash tables for storage

# Lists:
# - Can contain duplicates
# - Maintain order of elements
# - Membership testing takes O(n) time in the worst case

# Example of Set vs List
numbers_list = [1, 2, 3, 3, 2, 1]
numbers_set = {1, 2, 3}

print(f"List with duplicates: {numbers_list}")
print(f"Set with unique elements: {numbers_set}")

# 9. Time Complexity Summary
print("\n--- 9. TIME COMPLEXITY SUMMARY ---")
print("Operation                         | Time Complexity")
print("---------------------------------- | ----------------")
print("Add (set.add(x))                  | O(1) average case")
print("Remove (set.remove(x))            | O(1) average case")
print("Discard (set.discard(x))          | O(1) average case")
print("Pop (set.pop())                   | O(1) average case")
print("Union (set.union(s))              | O(n + m) where n, m are lengths of sets")
print("Intersection (set.intersection(s))| O(min(n, m))")
print("Difference (set.difference(s))    | O(n)")
print("Symmetric difference (set.symmetric_difference(s)) | O(n + m)")
print("Membership (x in set)             | O(1) average case")
print("Iteration (for x in set)          | O(n)")

print("\nThis guide covers the most common operations and use cases for Python sets.")
