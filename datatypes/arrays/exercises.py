"""
Python Arrays: Exercises and Solutions
-------------------------------------

This document contains practice exercises for Python arrays with detailed solutions.
Each exercise is designed to reinforce understanding of array operations and their time complexity.
"""

import array
import numpy as np  # If NumPy is not installed, run: pip install numpy

# -----------------------------------------------------
# EXERCISE 1: Basic Array Operations
# -----------------------------------------------------
print("\n--- EXERCISE 1: Basic Array Operations ---")
print("Problem: Create an array of integers from 1 to 10. Then:")
print("1. Print the 3rd element")
print("2. Print the last 3 elements")
print("3. Double each element in the array")
print("4. Calculate the sum and average of all elements")

# Solution to Exercise 1
def exercise1_solution():
    # Create the array (time complexity: O(n))
    int_array = array.array('i', range(1, 11))
    print(f"Original array: {int_array}")
    
    # 1. Print the 3rd element (time complexity: O(1))
    print(f"3rd element: {int_array[2]}")
    
    # 2. Print the last 3 elements (time complexity: O(k) where k is slice size)
    print(f"Last 3 elements: {int_array[-3:]}")
    
    # 3. Double each element in the array (time complexity: O(n))
    # Need to create a new array or modify in place
    for i in range(len(int_array)):
        int_array[i] *= 2
    print(f"After doubling each element: {int_array}")
    
    # 4. Calculate the sum and average (time complexity: O(n))
    array_sum = sum(int_array)
    array_avg = array_sum / len(int_array)
    print(f"Sum: {array_sum}, Average: {array_avg}")

exercise1_solution()

# -----------------------------------------------------
# EXERCISE 2: Array Type Conversion
# -----------------------------------------------------
print("\n--- EXERCISE 2: Array Type Conversion ---")
print("Problem: Perform the following conversions:")
print("1. Create an integer array and convert it to a float array")
print("2. Convert a list to an array and back to a list")
print("3. Convert between signed and unsigned integer arrays")
print("4. Create an array from a string of ASCII characters")

# Solution to Exercise 2
def exercise2_solution():
    # 1. Convert integer array to float array (time complexity: O(n))
    int_array = array.array('i', [1, 2, 3, 4, 5])
    float_array = array.array('f', [float(x) for x in int_array])
    print(f"Integer array: {int_array}")
    print(f"Float array: {float_array}")
    
    # 2. Convert list to array and back (time complexity: O(n) each way)
    my_list = [10, 20, 30, 40, 50]
    my_array = array.array('i', my_list)
    back_to_list = my_array.tolist()
    print(f"Original list: {my_list}")
    print(f"As array: {my_array}")
    print(f"Back to list: {back_to_list}")
    
    # 3. Convert between signed and unsigned (time complexity: O(n))
    signed = array.array('i', [1, 2, 3, 4, 5])
    # Need to ensure values are valid for unsigned
    unsigned = array.array('I', [x if x >= 0 else 0 for x in signed])
    print(f"Signed array: {signed}")
    print(f"Unsigned array: {unsigned}")
    
    # 4. Create array from string (time complexity: O(n))
    text = "Hello"
    char_array = array.array('B', [ord(c) for c in text])
    print(f"String: {text}")
    print(f"ASCII array: {char_array}")
    print(f"Back to string: {''.join(chr(c) for c in char_array)}")

exercise2_solution()

# -----------------------------------------------------
# EXERCISE 3: NumPy Array Creation
# -----------------------------------------------------
print("\n--- EXERCISE 3: NumPy Array Creation ---")
print("Problem: Create NumPy arrays in the following ways:")
print("1. Create a 1D array of evenly spaced values between 0 and 1 (5 values)")
print("2. Create a 3x3 identity matrix")
print("3. Create an array of random integers between 1 and 100 (size 10)")
print("4. Create a 2D array with a specific shape from a 1D array")

# Solution to Exercise 3
def exercise3_solution():
    # 1. Evenly spaced values (time complexity: O(n))
    linspace_array = np.linspace(0, 1, 5)
    print(f"Evenly spaced values between 0 and 1: {linspace_array}")
    
    # 2. Identity matrix (time complexity: O(n²))
    identity_matrix = np.eye(3)
    print("3x3 Identity matrix:")
    print(identity_matrix)
    
    # 3. Random integers (time complexity: O(n))
    random_ints = np.random.randint(1, 101, size=10)
    print(f"Random integers between 1 and 100: {random_ints}")
    
    # 4. Reshape 1D to 2D (time complexity: O(n))
    original = np.arange(1, 13)  # 1 to 12
    reshaped = original.reshape(3, 4)  # 3 rows, 4 columns
    print(f"Original 1D array: {original}")
    print("Reshaped to 3x4 array:")
    print(reshaped)

exercise3_solution()

# -----------------------------------------------------
# EXERCISE 4: NumPy Array Operations
# -----------------------------------------------------
print("\n--- EXERCISE 4: NumPy Array Operations ---")
print("Problem: Given a NumPy array, perform the following operations:")
print("1. Find the mean, median, max, and min values")
print("2. Perform element-wise operations (add 5, multiply by 2)")
print("3. Filter out all values below the mean")
print("4. Apply a mathematical function (e.g., square root) to each element")

# Solution to Exercise 4
def exercise4_solution():
    # Create a test array (time complexity: O(n))
    arr = np.array([14, 23, 32, 41, 50, 67, 76, 89, 95])
    print(f"Original array: {arr}")
    
    # 1. Statistics (all O(n))
    print(f"Mean: {np.mean(arr)}")
    print(f"Median: {np.median(arr)}")
    print(f"Max: {np.max(arr)}")
    print(f"Min: {np.min(arr)}")
    
    # 2. Element-wise operations (all O(n))
    print(f"Add 5 to each: {arr + 5}")
    print(f"Multiply each by 2: {arr * 2}")
    
    # 3. Filter below mean (time complexity: O(n))
    mean_value = np.mean(arr)
    above_mean = arr[arr > mean_value]
    print(f"Values above mean ({mean_value}): {above_mean}")
    
    # 4. Apply math function (time complexity: O(n))
    sqrt_values = np.sqrt(arr)
    print(f"Square root of each value: {sqrt_values}")

exercise4_solution()

# -----------------------------------------------------
# EXERCISE 5: 2D Array Manipulation
# -----------------------------------------------------
print("\n--- EXERCISE 5: 2D Array Manipulation ---")
print("Problem: Given a 2D NumPy array/matrix, perform the following:")
print("1. Calculate the sum of each row and each column")
print("2. Extract the diagonal elements")
print("3. Transpose the matrix")
print("4. Calculate the determinant (if square matrix)")

# Solution to Exercise 5
def exercise5_solution():
    # Create a 3x3 matrix (time complexity: O(n²))
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print("Original matrix:")
    print(matrix)
    
    # 1. Sum of rows and columns (time complexity: O(n²))
    row_sums = np.sum(matrix, axis=1)  # Sum across columns (for each row)
    col_sums = np.sum(matrix, axis=0)  # Sum across rows (for each column)
    print(f"Sum of each row: {row_sums}")
    print(f"Sum of each column: {col_sums}")
    
    # 2. Extract diagonal (time complexity: O(n))
    diag = np.diag(matrix)
    print(f"Diagonal elements: {diag}")
    
    # 3. Transpose (time complexity: O(n²))
    transposed = matrix.T
    print("Transposed matrix:")
    print(transposed)
    
    # 4. Determinant (time complexity: O(n³) for general case)
    det = np.linalg.det(matrix)
    print(f"Determinant: {det}")
    
    # Create a non-singular matrix for better determinant example
    non_singular = np.array([
        [1, 2, 3],
        [0, 4, 5],
        [0, 0, 6]
    ])
    print("Non-singular matrix:")
    print(non_singular)
    print(f"Determinant of non-singular matrix: {np.linalg.det(non_singular)}")

exercise5_solution()

# -----------------------------------------------------
# EXERCISE 6: Advanced NumPy Operations
# -----------------------------------------------------
print("\n--- EXERCISE 6: Advanced NumPy Operations ---")
print("Problem: Perform these advanced operations:")
print("1. Perform matrix multiplication between two matrices")
print("2. Compute eigenvalues and eigenvectors of a matrix")
print("3. Solve a system of linear equations using NumPy")
print("4. Perform singular value decomposition on a matrix")

# Solution to Exercise 6
def exercise6_solution():
    # Create test matrices
    A = np.array([
        [3, 1], 
        [2, 4]
    ])
    
    B = np.array([
        [1, 0],
        [2, 3]
    ])
    
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    
    # 1. Matrix multiplication (time complexity: depends on algorithm, generally O(n³) for naive implementation)
    C = np.dot(A, B)  # or A @ B in newer Python versions
    print("A × B:")
    print(C)
    
    # 2. Eigenvalues and eigenvectors (time complexity: O(n³))
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print("Eigenvalues of A:")
    print(eigenvalues)
    print("Eigenvectors of A:")
    print(eigenvectors)
    
    # 3. Solve linear equations: Ax = b (time complexity: O(n³))
    b = np.array([5, 8])
    x = np.linalg.solve(A, b)
    print(f"Solution to Ax = b where b = {b}:")
    print(f"x = {x}")
    
    # Verify the solution
    print(f"A @ x = {A @ x}, which should equal b = {b}")
    
    # 4. Singular value decomposition (time complexity: O(n³))
    U, S, Vh = np.linalg.svd(A)
    print("Singular Value Decomposition of A:")
    print("U (left singular vectors):")
    print(U)
    print("S (singular values):")
    print(S)
    print("Vh (right singular vectors transposed):")
    print(Vh)

exercise6_solution()

# -----------------------------------------------------
# EXERCISE 7: Memory and Performance with Arrays
# -----------------------------------------------------
print("\n--- EXERCISE 7: Memory and Performance with Arrays ---")
print("Problem: Compare the performance of Python lists vs arrays:")
print("1. Compare the memory usage of a list vs. a NumPy array")
print("2. Compare the time to compute the sum of all elements")
print("3. Compare element-wise multiplication performance")
print("4. Test slicing operations performance")

# Solution to Exercise 7
def exercise7_solution():
    import sys
    import time
    
    # Create test data structures of reasonable size
    size = 10000
    py_list = list(range(size))
    array_int = array.array('i', range(size))
    np_array = np.arange(size)
    
    # 1. Compare memory usage
    list_memory = sys.getsizeof(py_list)
    array_memory = sys.getsizeof(array_int)
    np_memory = sys.getsizeof(np_array) + np_array.nbytes  # Need to include the data buffer for numpy
    
    print(f"Memory usage for {size} elements:")
    print(f"Python list: {list_memory} bytes")
    print(f"Array: {array_memory} bytes")
    print(f"NumPy array: {np_memory} bytes")
    
    # 2. Compare sum performance
    start_time = time.time()
    list_sum = sum(py_list)
    list_time = time.time() - start_time
    
    start_time = time.time()
    array_sum = sum(array_int)
    array_time = time.time() - start_time
    
    start_time = time.time()
    np_sum = np.sum(np_array)
    np_time = time.time() - start_time
    
    print("\nTime to sum all elements:")
    print(f"Python list: {list_time:.6f} seconds")
    print(f"Array: {array_time:.6f} seconds")
    print(f"NumPy array: {np_time:.6f} seconds")
    
    # 3. Element-wise multiplication
    # For a fair comparison, use a smaller size
    size = 1000
    py_list = list(range(size))
    array_int = array.array('i', range(size))
    np_array = np.arange(size)
    
    start_time = time.time()
    list_mult = [x * 2 for x in py_list]
    list_time = time.time() - start_time
    
    start_time = time.time()
    array_mult = array.array('i', (x * 2 for x in array_int))
    array_time = time.time() - start_time
    
    start_time = time.time()
    np_mult = np_array * 2
    np_time = time.time() - start_time
    
    print("\nTime for element-wise multiplication:")
    print(f"Python list: {list_time:.6f} seconds")
    print(f"Array: {array_time:.6f} seconds")
    print(f"NumPy array: {np_time:.6f} seconds")
    
    # 4. Slicing operations
    start_time = time.time()
    list_slice = py_list[100:900]
    list_time = time.time() - start_time
    
    start_time = time.time()
    array_slice = array_int[100:900]
    array_time = time.time() - start_time
    
    start_time = time.time()
    np_slice = np_array[100:900]
    np_time = time.time() - start_time
    
    print("\nTime for slicing operations:")
    print(f"Python list: {list_time:.6f} seconds")
    print(f"Array: {array_time:.6f} seconds")
    print(f"NumPy array: {np_time:.6f} seconds")

exercise7_solution()

# -----------------------------------------------------
# EXERCISE 8: Practical Array Applications
# -----------------------------------------------------
print("\n--- EXERCISE 8: Practical")