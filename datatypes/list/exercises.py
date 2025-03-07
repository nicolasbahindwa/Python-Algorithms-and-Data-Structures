"""
Python Lists: Exercises and Solutions
------------------------------------

This document contains practice exercises for Python lists with detailed solutions.
Each exercise is designed to reinforce understanding of list operations and their time complexity.
"""

# -----------------------------------------------------
# EXERCISE 1: Basic List Operations
# -----------------------------------------------------
print("\n--- EXERCISE 1: Basic List Operations ---")
print("Problem: Create a list of the first 10 square numbers (1, 4, 9, etc.). Then:")
print("1. Print the 3rd element")
print("2. Print the last 3 elements using negative indexing")
print("3. Print all elements from index 2 to 7")

# Solution to Exercise 1
def exercise1_solution():
    # Create the list of squares (time complexity: O(n))
    squares = [i**2 for i in range(1, 11)]
    print(f"Original list: {squares}")
    
    # 1. Print the 3rd element (time complexity: O(1))
    print(f"3rd element: {squares[2]}")
    
    # 2. Print the last 3 elements using negative indexing (time complexity: O(1) for each access)
    print(f"Last 3 elements: {squares[-3:]}")
    
    # 3. Print all elements from index 2 to 7 (time complexity: O(k) where k is slice size)
    print(f"Elements from index 2 to 7: {squares[2:8]}")

exercise1_solution()

# -----------------------------------------------------
# EXERCISE 2: List Modification
# -----------------------------------------------------
print("\n--- EXERCISE 2: List Modification ---")
print("Problem: Start with the list [10, 20, 30, 40, 50].")
print("1. Add 60 to the end")
print("2. Insert 15 between 10 and 20")
print("3. Remove the element 30")
print("4. Replace 40 with 45")
print("5. Sort the list in descending order")

# Solution to Exercise 2
def exercise2_solution():
    # Create the initial list
    my_list = [10, 20, 30, 40, 50]
    print(f"Original list: {my_list}")
    
    # 1. Add 60 to the end (time complexity: O(1) amortized)
    my_list.append(60)
    print(f"After append(60): {my_list}")
    
    # 2. Insert 15 between 10 and 20 (time complexity: O(n))
    my_list.insert(1, 15)
    print(f"After insert(1, 15): {my_list}")
    
    # 3. Remove the element 30 (time complexity: O(n))
    my_list.remove(30)
    print(f"After remove(30): {my_list}")
    
    # 4. Replace 40 with 45 (time complexity: O(n) for finding, O(1) for assignment)
    index = my_list.index(40)
    my_list[index] = 45
    print(f"After replacing 40 with 45: {my_list}")
    
    # 5. Sort the list in descending order (time complexity: O(n log n))
    my_list.sort(reverse=True)
    print(f"After sorting in descending order: {my_list}")

exercise2_solution()

# -----------------------------------------------------
# EXERCISE 3: List Comprehension
# -----------------------------------------------------
print("\n--- EXERCISE 3: List Comprehension ---")
print("Problem: Use list comprehension to:")
print("1. Create a list of all even numbers from 1 to 20")
print("2. Create a list of squares of even numbers from 1 to 10")
print("3. Create a list of tuples containing (number, square) for numbers 1-5")
print("4. Filter out all words starting with 'a' from ['apple', 'banana', 'avocado', 'orange']")

# Solution to Exercise 3
def exercise3_solution():
    # 1. Create a list of all even numbers from 1 to 20 (time complexity: O(n))
    even_numbers = [i for i in range(1, 21) if i % 2 == 0]
    print(f"Even numbers from 1 to 20: {even_numbers}")
    
    # 2. Create a list of squares of even numbers from 1 to 10 (time complexity: O(n))
    even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
    print(f"Squares of even numbers from 1 to 10: {even_squares}")
    
    # 3. Create a list of tuples containing (number, square) for numbers 1-5 (time complexity: O(n))
    number_tuples = [(i, i**2) for i in range(1, 6)]
    print(f"List of (number, square) tuples: {number_tuples}")
    
    # 4. Filter out all words starting with 'a' from a list (time complexity: O(n))
    fruits = ['apple', 'banana', 'avocado', 'orange']
    filtered_fruits = [fruit for fruit in fruits if not fruit.startswith('a')]
    print(f"Fruits not starting with 'a': {filtered_fruits}")

exercise3_solution()

# -----------------------------------------------------
# EXERCISE 4: Working with Nested Lists
# -----------------------------------------------------
print("\n--- EXERCISE 4: Working with Nested Lists ---")
print("Problem: Given a 3x3 matrix represented as a nested list:")
print("[[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
print("1. Calculate the sum of all elements")
print("2. Calculate the sum of each row")
print("3. Calculate the sum of each column")
print("4. Find the maximum value in the matrix")
print("5. Extract the diagonal elements (1, 5, 9)")

# Solution to Exercise 4
def exercise4_solution():
    # Define the matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    # 1. Calculate the sum of all elements (time complexity: O(n*m))
    total_sum = sum(sum(row) for row in matrix)
    print(f"Sum of all elements: {total_sum}")
    
    # 2. Calculate the sum of each row (time complexity: O(n*m))
    row_sums = [sum(row) for row in matrix]
    print(f"Sum of each row: {row_sums}")
    
    # 3. Calculate the sum of each column (time complexity: O(n*m))
    column_sums = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
    print(f"Sum of each column: {column_sums}")
    
    # 4. Find the maximum value in the matrix (time complexity: O(n*m))
    max_value = max(max(row) for row in matrix)
    print(f"Maximum value: {max_value}")
    
    # 5. Extract the diagonal elements (time complexity: O(n))
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    print(f"Diagonal elements: {diagonal}")
    
    # Bonus: Extract the other diagonal (time complexity: O(n))
    other_diagonal = [matrix[i][len(matrix)-1-i] for i in range(len(matrix))]
    print(f"Other diagonal elements: {other_diagonal}")

exercise4_solution()

# -----------------------------------------------------
# EXERCISE 5: List Algorithms
# -----------------------------------------------------
print("\n--- EXERCISE 5: List Algorithms ---")
print("Problem: Implement the following algorithms using lists:")
print("1. Find the second largest element in a list")
print("2. Remove duplicates from a list while preserving order")
print("3. Merge two sorted lists into a single sorted list")
print("4. Find all pairs of numbers in a list that sum to a given target")

# Solution to Exercise 5
def exercise5_solution():
    # Test data
    numbers = [3, 8, 1, 7, 2, 9, 5, 4, 6, 8, 3]
    print(f"Original list: {numbers}")
    
    # 1. Find the second largest element (time complexity: O(n))
    def second_largest(lst):
        if len(lst) < 2:
            return None
        max_val = second_max = float('-inf')
        for num in lst:
            if num > max_val:
                second_max = max_val
                max_val = num
            elif num > second_max and num < max_val:
                second_max = num
        return second_max if second_max != float('-inf') else None
    
    print(f"Second largest element: {second_largest(numbers)}")
    
    # 2. Remove duplicates while preserving order (time complexity: O(n))
    def remove_duplicates(lst):
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    print(f"List with duplicates removed: {remove_duplicates(numbers)}")
    
    # 3. Merge two sorted lists (time complexity: O(n+m))
    def merge_sorted_lists(list1, list2):
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result
    
    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]
    print(f"Merged sorted lists: {merge_sorted_lists(list1, list2)}")
    
    # 4. Find all pairs that sum to target (time complexity: O(n²) naive implementation)
    def find_pairs(lst, target):
        pairs = []
        # More efficient with a set, but using traditional approach for clarity
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] + lst[j] == target:
                    pairs.append((lst[i], lst[j]))
        return pairs
    
    print(f"Pairs that sum to 10: {find_pairs(numbers, 10)}")
    
    # 4b. More efficient implementation using a set (time complexity: O(n))
    def find_pairs_efficient(lst, target):
        pairs = []
        seen = set()
        for num in lst:
            complement = target - num
            if complement in seen:
                pairs.append((complement, num))
            seen.add(num)
        return pairs
    
    print(f"Pairs that sum to 10 (efficient): {find_pairs_efficient(numbers, 10)}")

exercise5_solution()

# -----------------------------------------------------
# EXERCISE 6: Advanced List Operations
# -----------------------------------------------------
print("\n--- EXERCISE 6: Advanced List Operations ---")
print("Problem: Perform these advanced operations:")
print("1. Flatten a list of lists into a single list")
print("2. Group a list of numbers into sublists of a specific size")
print("3. Implement a simple moving average calculator")
print("4. Rotate a list by k positions")

# Solution to Exercise 6
def exercise6_solution():
    # Test data
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 1. Flatten a list of lists (time complexity: O(n) where n is total elements)
    def flatten(nested):
        return [item for sublist in nested for item in sublist]
    
    print(f"Original nested list: {nested_list}")
    print(f"Flattened list: {flatten(nested_list)}")
    
    # 2. Group a list into chunks (time complexity: O(n))
    def chunk_list(lst, chunk_size):
        return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
    
    print(f"List chunked into groups of 3: {chunk_list(numbers, 3)}")
    
    # 3. Moving average calculator (time complexity: O(n))
    def moving_average(lst, window_size):
        results = []
        for i in range(len(lst) - window_size + 1):
            window = lst[i:i+window_size]
            avg = sum(window) / window_size
            results.append(avg)
        return results
    
    print(f"Moving average (window size 3): {moving_average(numbers, 3)}")
    
    # 4. Rotate a list by k positions (time complexity: O(n))
    def rotate_list(lst, k):
        k = k % len(lst)  # Handle k > len(lst)
        return lst[-k:] + lst[:-k]
    
    print(f"List rotated by 3 positions: {rotate_list(numbers, 3)}")

exercise6_solution()

# -----------------------------------------------------
# EXERCISE 7: Functional Programming with Lists
# -----------------------------------------------------
print("\n--- EXERCISE 7: Functional Programming with Lists ---")
print("Problem: Use functional programming techniques with lists:")
print("1. Use map to square each element in a list")
print("2. Use filter to get only even numbers from a list")
print("3. Use reduce to find the product of all numbers in a list")
print("4. Chain these operations together")

# Solution to Exercise 7
def exercise7_solution():
    from functools import reduce
    
    # Test data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original list: {numbers}")
    
    # 1. Use map to square each element (time complexity: O(n))
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squared numbers: {squared}")
    
    # 2. Use filter to get only even numbers (time complexity: O(n))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {evens}")
    
    # 3. Use reduce to find the product of all numbers (time complexity: O(n))
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product of all numbers: {product}")
    
    # 4. Chain these operations together (time complexity: O(n))
    # Get the product of squares of even numbers
    result = reduce(
        lambda x, y: x * y,
        map(lambda x: x**2,
            filter(lambda x: x % 2 == 0, numbers)
        )
    )
    print(f"Product of squares of even numbers: {result}")

exercise7_solution()

print("\nComplete all exercises to master Python lists!")