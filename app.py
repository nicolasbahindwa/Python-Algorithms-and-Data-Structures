"""
PYTHON BASIC ALGORITHMS
=======================

This file covers fundamental algorithms implemented in Python, including:
1. Searching Algorithms
2. Sorting Algorithms 
3. String Manipulation
4. Basic Data Structure Algorithms
5. Numeric and Mathematical Algorithms
6. Graph Algorithms
7. Dynamic Programming
"""

# =============================================================================
# 1. SEARCHING ALGORITHMS
# =============================================================================

def linear_search(arr, target):
    """
    Linear Search: Check each element sequentially until finding the target.
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: List of elements to search through
        target: Element to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Binary Search: Search a sorted array by repeatedly dividing the search interval in half.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr: Sorted list of elements to search through
        target: Element to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is at the middle
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    # Element not present
    return -1

def binary_search_recursive(arr, target, left, right):
    """
    Recursive implementation of Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    
    Args:
        arr: Sorted list of elements to search through
        target: Element to find
        left: Left boundary index
        right: Right boundary index
        
    Returns:
        Index of target if found, -1 otherwise
    """
    # Base case: element not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # If element is at mid
    if arr[mid] == target:
        return mid
    
    # If element is smaller than mid, search in left subarray
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Else search in right subarray
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Example usage of search algorithms
def search_examples():
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = 23
    
    # Linear search
    linear_result = linear_search(arr, target)
    print(f"Linear Search: Element {target} found at index {linear_result}")
    
    # Binary search (iterative)
    binary_result = binary_search(arr, target)
    print(f"Binary Search: Element {target} found at index {binary_result}")
    
    # Binary search (recursive)
    recursive_result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Recursive Binary Search: Element {target} found at index {recursive_result}")

# =============================================================================
# 2. SORTING ALGORITHMS
# =============================================================================

def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly steps through the list, compares adjacent elements 
                and swaps them if they are in the wrong order.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        arr: List of elements to sort
        
    Returns:
        Sorted list
    """
    n = len(arr)
    # Make a copy to avoid modifying the original
    result = arr.copy()
    
    for i in range(n):
        # Flag to optimize if no swaps are made in a pass
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
                
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
            
    return result

def selection_sort(arr):
    """
    Selection Sort: Repeatedly finds the minimum element from unsorted part
                   and puts it at the beginning.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        arr: List of elements to sort
        
    Returns:
        Sorted list
    """
    n = len(arr)
    result = arr.copy()
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        result[i], result[min_idx] = result[min_idx], result[i]
        
    return result

def insertion_sort(arr):
    """
    Insertion Sort: Build sorted array one item at a time by inserting 
                   each new item in its proper place.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        arr: List of elements to sort
        
    Returns:
        Sorted list
    """
    result = arr.copy()
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(result)):
        key = result[i]
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < result[j]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
        
    return result

def merge_sort(arr):
    """
    Merge Sort: Divide array into two halves, sort them and merge.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr: List of elements to sort
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """Helper function for merge sort to merge two sorted arrays"""
    result = []
    i = j = 0
    
    # Compare elements from both arrays and add smaller to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def quick_sort(arr):
    """
    Quick Sort: Select a 'pivot' element and partition the array around it.
    Time Complexity: Average O(n log n), Worst case O(n²)
    Space Complexity: O(log n) for recursion stack
    
    Args:
        arr: List of elements to sort
        
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Create a copy to avoid modifying the original
    result = arr.copy()
    quick_sort_helper(result, 0, len(result) - 1)
    return result

def quick_sort_helper(arr, low, high):
    """Helper function for quick sort implementation"""
    if low < high:
        # Partition array and get pivot position
        pivot_idx = partition(arr, low, high)
        
        # Sort elements before and after pivot
        quick_sort_helper(arr, low, pivot_idx - 1)
        quick_sort_helper(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    """Helper function for quick sort to partition the array"""
    # Choose rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in its final position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def counting_sort(arr, max_val=None):
    """
    Counting Sort: Sort elements based on their frequency count.
    Only works for non-negative integers.
    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(n + k)
    
    Args:
        arr: List of non-negative integers to sort
        max_val: Maximum value in the array (computed if not provided)
        
    Returns:
        Sorted list
    """
    if not arr:
        return []
    
    # Find the maximum value if not provided
    if max_val is None:
        max_val = max(arr)
    
    # Initialize count array with zeros
    count = [0] * (max_val + 1)
    
    # Store count of each element
    for num in arr:
        count[num] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

# Example usage of sorting algorithms
def sorting_examples():
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    # Bubble sort
    bubble_sorted = bubble_sort(arr)
    print(f"Bubble Sort: {bubble_sorted}")
    
    # Selection sort
    selection_sorted = selection_sort(arr)
    print(f"Selection Sort: {selection_sorted}")
    
    # Insertion sort
    insertion_sorted = insertion_sort(arr)
    print(f"Insertion Sort: {insertion_sorted}")
    
    # Merge sort
    merge_sorted = merge_sort(arr)
    print(f"Merge Sort: {merge_sorted}")
    
    # Quick sort
    quick_sorted = quick_sort(arr)
    print(f"Quick Sort: {quick_sorted}")
    
    # Counting sort (only for non-negative integers)
    counting_sorted = counting_sort(arr)
    print(f"Counting Sort: {counting_sorted}")

# =============================================================================
# 3. STRING MANIPULATION ALGORITHMS
# =============================================================================

def string_reverse(s):
    """
    Reverse a string.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        s: String to reverse
        
    Returns:
        Reversed string
    """
    # Python has built-in string reversal using slicing
    return s[::-1]
    
    # Alternative manual implementation
    # result = ""
    # for char in s:
    #     result = char + result
    # return result

def is_palindrome(s):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        s: String to check
        
    Returns:
        True if string is a palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the string equals its reverse
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def longest_common_prefix(strs):
    """
    Find the longest common prefix string amongst an array of strings.
    Time Complexity: O(n * m) where n is number of strings and m is length of shortest string
    Space Complexity: O(1)
    
    Args:
        strs: List of strings
        
    Returns:
        Longest common prefix
    """
    if not strs:
        return ""
    
    # Start with the first string as the potential prefix
    prefix = strs[0]
    
    # Compare with remaining strings
    for string in strs[1:]:
        # Reduce prefix until it matches the beginning of the current string
        while string.find(prefix) != 0:
            prefix = prefix[:-1]
            
            # If prefix becomes empty, there is no common prefix
            if not prefix:
                return ""
    
    return prefix

def is_anagram(s1, s2):
    """
    Check if two strings are anagrams (contain the same characters with same frequency).
    Time Complexity: O(n)
    Space Complexity: O(k) where k is size of the character set
    
    Args:
        s1: First string
        s2: Second string
        
    Returns:
        True if strings are anagrams, False otherwise
    """
    # Remove spaces and convert to lowercase
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    
    # Check if lengths are different
    if len(s1) != len(s2):
        return False
    
    # Count character frequencies
    char_count = {}
    
    # Count characters in first string
    for char in s1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Check characters in second string
    for char in s2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True

def string_pattern_search(text, pattern):
    """
    Simple pattern matching algorithm to find all occurrences of a pattern in text.
    Time Complexity: O(n * m) where n is text length, m is pattern length
    Space Complexity: O(1)
    
    Args:
        text: String to search in
        pattern: Pattern to search for
        
    Returns:
        List of starting indices where pattern occurs
    """
    indices = []
    
    # If pattern is empty or longer than text
    if not pattern or len(pattern) > len(text):
        return indices
    
    # Slide pattern over text and check for matches
    for i in range(len(text) - len(pattern) + 1):
        match = True
        
        # Check each character of pattern with text
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
        
        # If pattern matched, add the starting index
        if match:
            indices.append(i)
    
    return indices

# Example usage of string algorithms
def string_examples():
    # String reversal
    original = "Hello, World!"
    reversed_str = string_reverse(original)
    print(f"Original: '{original}', Reversed: '{reversed_str}'")
    
    # Palindrome check
    palindrome = "A man, a plan, a canal: Panama"
    not_palindrome = "Hello, World!"
    print(f"Is '{palindrome}' a palindrome? {is_palindrome(palindrome)}")
    print(f"Is '{not_palindrome}' a palindrome? {is_palindrome(not_palindrome)}")
    
    # Longest common prefix
    string_array = ["flower", "flow", "flight"]
    prefix = longest_common_prefix(string_array)
    print(f"Longest common prefix of {string_array}: '{prefix}'")
    
    # Anagram check
    s1 = "listen"
    s2 = "silent"
    print(f"Are '{s1}' and '{s2}' anagrams? {is_anagram(s1, s2)}")
    
    # Pattern search
    text = "ABABDABACDABABCABAB"
    pattern = "ABABC"
    occurrences = string_pattern_search(text, pattern)
    print(f"Pattern '{pattern}' found at indices: {occurrences}")

# =============================================================================
# 4. BASIC DATA STRUCTURE ALGORITHMS
# =============================================================================

class Stack:
    """Stack implementation using a Python list"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)

class Queue:
    """Queue implementation using a Python list"""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)
    
    def front(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.items[0]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)

def balanced_parentheses(expr):
    """
    Check if parentheses in an expression are balanced.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        expr: String expression containing parentheses '(', ')', '{', '}', '[', ']'
        
    Returns:
        True if parentheses are balanced, False otherwise
    """
    stack = Stack()
    
    # Dictionary to store pairs of opening and closing brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expr:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.push(char)
        
        # If it's a closing bracket
        elif char in ')}]':
            # Check if stack is empty or mismatched bracket
            if stack.is_empty() or stack.pop() != brackets[char]:
                return False
    
    # Check if all brackets were matched
    return stack.is_empty()

# Example usage of data structure algorithms
def data_structure_examples():
    # Stack operations
    print("=== Stack Example ===")
    stack = Stack()
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(f"Stack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    print(f"Popped element: {stack.pop()}")
    print(f"Stack size after pop: {stack.size()}")
    
    # Queue operations
    print("\n=== Queue Example ===")
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    print(f"Queue size: {queue.size()}")
    print(f"Front element: {queue.front()}")
    print(f"Dequeued element: {queue.dequeue()}")
    print(f"Queue size after dequeue: {queue.size()}")
    
    # Balanced parentheses
    print("\n=== Balanced Parentheses Example ===")
    expressions = [
        "{[()]}",
        "{[(])}",
        "((()))",
        "(()"
    ]
    
    for expr in expressions:
        result = balanced_parentheses(expr)
        print(f"Expression '{expr}' has balanced parentheses: {result}")

# =============================================================================
# 5. NUMERIC AND MATHEMATICAL ALGORITHMS
# =============================================================================

def factorial(n):
    """
    Calculate factorial of n (n!).
    Time Complexity: O(n)
    Space Complexity: O(1) for iterative, O(n) for recursive due to call stack
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Iterative implementation
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result

def fibonacci(n):
    """
    Calculate the nth Fibonacci number iteratively.
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Non-negative integer position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number recursively.
    Time Complexity: O(2^n) - exponential!
    Space Complexity: O(n) due to recursion stack
    
    Args:
        n: Non-negative integer position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    
    if n <= 1:
        return n
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, memo=None):
    """
    Calculate the nth Fibonacci number using memoization to avoid redundant calculations.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Non-negative integer position in Fibonacci sequence
        memo: Dictionary to store previously computed values
        
    Returns:
        nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

def is_prime(n):
    """
    Check if a number is prime.
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    # Check if n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check all numbers of form 6k ± 1 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def gcd(a, b):
    """
    Calculate the greatest common divisor using Euclidean algorithm.
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(log(min(a, b))) for recursion
    
    Args:
        a, b: Integers
        
    Returns:
        Greatest common divisor of a and b
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    """
    Calculate the least common multiple using GCD.
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(log(min(a, b)))
    
    Args:
        a, b: Integers
        
    Returns:
        Least common multiple of a and b
    """
    return abs(a * b) // gcd(a, b)

# Example usage of mathematical algorithms
def math_examples():
    # Factorial
    n = 5
    fact = factorial(n)
    print(f"Factorial of {n}: {fact}")
    
    # Fibonacci (iterative)
    fib = fibonacci(10)
    print(f"10th Fibonacci number (iterative): {fib}")
    
    # Fibonacci (memoized)
    fib_memo = fibonacci_memoized(10)
    print(f"10th Fibonacci number (memoized): {fib_memo}")
    
    # Prime check
    numbers = [2, 7, 10, 17, 20]
    for num in numbers:
        print(f"Is {num} prime? {is_prime(num)}")
    
    # GCD
    a, b = 48, 18
    print(f"GCD of {a} and {b}: {gcd(a, b)}")
    
    # LCM
    print(f"LCM of {a} and {b}: {lcm(a, b)}")

# =============================================================================
# 6. GRAPH ALGORITHMS
# =============================================================================

def bfs(graph, start):
    """
    Breadth-First Search traversal of a graph.
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)
    
    Args:
        graph: Dictionary representing adjacency list of graph
        start: Starting vertex
        
    Returns:
        List of vertices in BFS order
    """
    if start not in graph:
        return []
    
    # Keep track of visited vertices
    visited = {start}
    
    # Queue for BFS
    queue = [start]
    
    # Result list
    result = []
    
    while queue:
        # Dequeue a vertex
        vertex = queue.pop(0)
        
        # Process the vertex
        result.append(vertex)
        
        # Visit all adjacent vertices
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

def dfs_recursive(graph, start, visited=None, result=None):
    """
    Depth-First Search traversal of a graph (recursive implementation).
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V) for recursion stack
    
    Args:
        graph: Dictionary representing adjacency list of graph
        start: Starting vertex
        visited: Set of visited vertices
        result: List to store traversal order
        
    Returns:
        List of vertices in DFS order
    """
    if start not in graph:
        return []
    
    if visited is None:
        visited = set()
    
    if result is None:
        result = []
    
    # Mark the current vertex as visited
    visited.add(start)
    
    # Process the vertex
    result.append(start)
    
    # Recur for all adjacent vertices
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    
    return result

def dfs_iterative(graph, start):
    """
    Depth-First Search traversal of a graph (iterative implementation).
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)
    
    Args:
        graph: Dictionary representing adjacency list of graph
        start: Starting vertex
        
    Returns:
        List of vertices in DFS order
    """
    if start not in graph:
        return []
    
    # Keep track of visited vertices
    visited = set()
    
    # Stack for DFS
    stack = [start]
    
    # Result list
    result = []
    
    while stack:
        # Pop a vertex from stack
        vertex = stack.pop()
        
        # If not visited, process it
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Push all neighbors to stack
            # Reverse order to match recursive DFS
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result

def shortest_path_bfs(graph, start, end):
    """
    Find shortest path between two vertices in an unweighted graph using BFS.
    Time Complexity: O(V + E) where V is vertices and E is edges
    Space Complexity: O(V)
    
    Args:
        graph: Dictionary representing adjacency list of graph
        start: Starting vertex
        end: Target vertex
        
    Returns:
        Shortest path as a list of vertices, or None if no path exists
    """
    if start not in graph or end not in graph:
        return None
    
    # Handle the case where start and end are the same
    if start == end:
        return [start]
    
    # Keep track of visited vertices and their predecessors
    visited = {start}
    queue = [start]
    
    # Dictionary to store path
    predecessor = {}
    
    while queue:
        current = queue.pop(0)
        
        # Check neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                predecessor[neighbor] = current
                
                # If we found the end vertex
                if neighbor == end:
                    # Reconstruct the path
                    path = [end]
                    while path[-1] != start:
                        path.append(predecessor[path[-1]])
                    
                    # Reverse to get path from start to end
                    path.reverse()
                    return path
    
    # No path found
    return None

 