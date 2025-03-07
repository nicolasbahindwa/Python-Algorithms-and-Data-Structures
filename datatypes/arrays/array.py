"""
Python Arrays: A Comprehensive Guide with Time Complexity
--------------------------------------------------------

This document explains the various operations, use cases, and time complexities
of Python arrays (both standard array module and NumPy arrays) with practical examples.
"""

import array
import sys
import time
import numpy as np  # If NumPy is not installed, run: pip install numpy

# 1. Introduction to Arrays
print("\n--- 1. INTRODUCTION TO ARRAYS ---")

# Python has two main array types:
# 1. `array` module from the standard library (typed arrays)
# 2. NumPy arrays (optimized numerical computing)

print("Arrays are more memory-efficient than lists for large numerical data")
print("Arrays enforce type consistency (all elements must be the same type)")

# 2. Array Module (Standard Library)
print("\n--- 2. ARRAY MODULE BASICS ---")

# Common typecodes:
# 'i' - signed int (typically 4 bytes)
# 'I' - unsigned int
# 'f' - float (typically 4 bytes)
# 'd' - double (typically 8 bytes)
# 'b' - signed char (1 byte)
# 'B' - unsigned char (1 byte)

# Creating arrays - O(n) where n is the number of elements
int_array = array.array('i', [1, 2, 3, 4, 5])  # O(n)
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])  # O(n)

print(f"Integer array: {int_array}")
print(f"Float array: {float_array}")

# Accessing elements - O(1) constant time
print(f"First element: {int_array[0]}")      # O(1)
print(f"Last element: {int_array[-1]}")      # O(1)
print(f"Slicing [1:3]: {int_array[1:3]}")    # O(k) where k is slice size

# 3. Array Operations and Methods
print("\n--- 3. ARRAY OPERATIONS AND METHODS ---")

# Adding elements
int_array.append(6)  # O(1) amortized - Add to end
print(f"After append(6): {int_array}")

int_array.extend([7, 8, 9])  # O(k) where k is length of sequence being added
print(f"After extend([7, 8, 9]): {int_array}")

int_array.insert(2, 10)  # O(n) - Insert at specific position
print(f"After insert(2, 10): {int_array}")

# Removing elements
popped_value = int_array.pop()  # O(1) - Remove and return last element
print(f"Popped value: {popped_value}")
print(f"After pop(): {int_array}")

popped_index = int_array.pop(2)  # O(n) - Remove at index (shifts elements)
print(f"Popped at index 2: {popped_index}")
print(f"After pop(2): {int_array}")

int_array.remove(4)  # O(n) - Remove first occurrence of value
print(f"After remove(4): {int_array}")

# Other operations
print(f"Array length: {len(int_array)}")  # O(1)
print(f"Count of 5: {int_array.count(5)}")  # O(n)
print(f"Index of 5: {int_array.index(5)}")  # O(n)

# Convert to list and back
list_version = int_array.tolist()  # O(n)
print(f"As list: {list_version}")

back_to_array = array.array('i', list_version)  # O(n)
print(f"Back to array: {back_to_array}")

# 4. Memory Efficiency Comparison
print("\n--- 4. MEMORY EFFICIENCY COMPARISON ---")

# Create equivalent data structures
test_size = 1000000
list_of_ints = list(range(test_size))  # O(n)
array_of_ints = array.array('i', range(test_size))  # O(n)

# Compare memory usage
print(f"Memory for list of {test_size} integers: {sys.getsizeof(list_of_ints)} bytes")
print(f"Memory for array of {test_size} integers: {sys.getsizeof(array_of_ints)} bytes")
print(f"Memory ratio: {sys.getsizeof(list_of_ints) / sys.getsizeof(array_of_ints):.2f}x")

# 5. Performance Comparison
print("\n--- 5. PERFORMANCE COMPARISON ---")

# Create smaller structures for timing tests
test_size = 100000
list_of_ints = list(range(test_size))  # O(n)
array_of_ints = array.array('i', range(test_size))  # O(n)

# Time list operations
start = time.time()
for i in range(1000):
    x = list_of_ints[i]  # O(1)
list_access_time = time.time() - start

# Time array operations
start = time.time()
for i in range(1000):
    x = array_of_ints[i]  # O(1)
array_access_time = time.time() - start

print(f"Time to access 1000 list elements: {list_access_time:.6f} seconds")
print(f"Time to access 1000 array elements: {array_access_time:.6f} seconds")

# 6. NumPy Arrays (ndarray)
print("\n--- 6. NUMPY ARRAYS ---")

# Creating NumPy arrays - O(n)
np_array1 = np.array([1, 2, 3, 4, 5])  # 1D array
np_array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 2D array

print(f"1D NumPy array: {np_array1}")
print("2D NumPy array:")
print(np_array2)

# Array properties
print(f"Shape: {np_array2.shape}")  # O(1)
print(f"Dimensions: {np_array2.ndim}")  # O(1)
print(f"Size (total elements): {np_array2.size}")  # O(1)
print(f"Data type: {np_array2.dtype}")  # O(1)

# 7. NumPy Array Operations
print("\n--- 7. NUMPY ARRAY OPERATIONS ---")

# Element-wise operations - O(n)
print(f"Original array: {np_array1}")
print(f"Add 5 to each element: {np_array1 + 5}")  # O(n)
print(f"Multiply each element by 2: {np_array1 * 2}")  # O(n)
print(f"Square each element: {np_array1 ** 2}")  # O(n)

# Array-wide operations - O(n)
print(f"Sum of all elements: {np.sum(np_array1)}")  # O(n)
print(f"Mean value: {np.mean(np_array1)}")  # O(n)
print(f"Maximum value: {np.max(np_array1)}")  # O(n)
print(f"Minimum value: {np.min(np_array1)}")  # O(n)

# 8. Indexing and Slicing NumPy Arrays
print("\n--- 8. INDEXING AND SLICING NUMPY ARRAYS ---")

# 2D array for demonstration
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original matrix:")
print(matrix)

# Basic indexing - O(1)
print(f"Element at (1,2): {matrix[1, 2]}")  # Row 1, Column 2 - O(1)

# Slicing - O(k) where k is the size of the slice
print("First row:")
print(matrix[0, :])  # First row, all columns - O(n)

print("Second column:")
print(matrix[:, 1])  # All rows, second column - O(n)

print("2x2 submatrix:")
print(matrix[1:3, 0:2])  # Rows 1-2, columns 0-1 - O(k)

# 9. Advanced NumPy Operations
print("\n--- 9. ADVANCED NUMPY OPERATIONS ---")

# Reshaping arrays - O(n)
original = np.array([1, 2, 3, 4, 5, 6])
reshaped = original.reshape(2, 3)  # Reshape to 2x3 matrix - O(n)
print("Original 1D array:", original)
print("Reshaped to 2x3:")
print(reshaped)

# Transposing matrices - O(n)
transposed = reshaped.T  # Transpose - O(n)
print("Transposed (3x2):")
print(transposed)

# Broadcasting (efficient operations between different shapes)
a = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3
b = np.array([10, 20, 30])  # 1D array of size 3
print("Matrix a:")
print(a)
print("Vector b:", b)
print("a + b (broadcasting):")
print(a + b)  # Broadcasting - O(n)

# Matrix operations
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print("Matrix multiplication:")
print(np.dot(m1, m2))  # Matrix multiplication - O(n³) for naive implementation

# 10. Creating Special Arrays
print("\n--- 10. CREATING SPECIAL ARRAYS ---")

# Zeros, ones, and identity matrices - All O(n)
zeros = np.zeros((2, 3))  # 2x3 matrix of zeros - O(n)
ones = np.ones((3, 2))  # 3x2 matrix of ones - O(n)
identity = np.eye(3)  # 3x3 identity matrix - O(n)
random_array = np.random.rand(2, 2)  # 2x2 matrix of random values - O(n)

print("Zeros matrix:")
print(zeros)
print("Ones matrix:")
print(ones)
print("Identity matrix:")
print(identity)
print("Random matrix:")
print(random_array)

# 11. Time Complexity Comparison Summary
print("\n--- 11. TIME COMPLEXITY COMPARISON SUMMARY ---")
print("Operation                      | List    | Array  | NumPy Array")
print("-------------------------------|---------|--------|------------")
print("Creation                       | O(n)    | O(n)   | O(n)")
print("Access by index                | O(1)    | O(1)   | O(1)")
print("Slicing                        | O(k)    | O(k)   | O(k)")
print("Append                         | O(1)*   | O(1)*  | O(n)")
print("Insert at position             | O(n)    | O(n)   | O(n)")
print("Delete                         | O(n)    | O(n)   | O(n)")
print("Iteration                      | O(n)    | O(n)   | O(n)")
print("Find (x in array)              | O(n)    | O(n)   | O(n)")
print("Memory per element             | High    | Low    | Low")
print("Element-wise operations        | O(n)**  | O(n)** | O(n)")
print("Matrix operations              | N/A     | N/A    | O(n³) or less***")
print("* Amortized constant time")
print("** Requires explicit loop in Lists and Arrays")
print("*** NumPy optimizes many operations below O(n³)")

print("\nThis guide covers common operations and use cases for Python arrays.")