"""
Python Deque: A Comprehensive Guide with Time Complexity
--------------------------------------------------------

This document explains the operations, use cases, and time complexities
of Python's deque (double-ended queue) with practical examples.
"""


from collections import deque

# 1. Creating a Deque
print("\n--- 1. CREATING A DEQUE ---")
 
# Initializing an empty deque - O(1)
dq = deque()  
print(f"Empty deque: {dq}")


# Initializing a deque with elements - O(n)
dq = deque([1,2,3,4,5])
print(f"dequee with element {dq}")

# 2. Adding Elements to a Dequee
dq.append(6)
print(f"Deque after append(6): {dq}")

# Append to the left - O(1)
dq.appendleft(0)
print(f"Deque after appendleft(0): {dq}")

# Extend multiple elements to the right - O(k)
dq.extend([7,8,9])
print(f"Deque after extend([7,8,9]): {dq}")

dq.appendleft(10)
print(dq)

# Extend multiple elements to the left (added in reverse order) - O(k)
dq.extendleft([-2, -1])
print(f"Deque after extendleft([-2,-1]): {dq}")


# 3. Removing Elements from a Deque
print("\n--- 3. REMOVING ELEMENTS ---")


# Pop from the right - O(1)
dq.pop()
print(f"Deque after pop(): {dq}")

# Pop from the left - O(1)
dq.popleft()
print(f"Deque after popleft(): {dq}")

dq.popleft()
print(f"Deque after popleft(): {dq}")

# Remove specific element (linear search required) - O(n)
dq.remove(3)  
print(f"Deque after remove(3): {dq}")


# 4. Accessing Elements
print("\n--- 4. ACCESSING ELEMENTS ---")

# Access elements by index (slow compared to list) - O(n)
print(f"Element at index 2: {dq[2]}")

# First and last elements - O(1)
print(f"First element: {dq[0]}")
print(f"Last element: {dq[-1]}")

# 5. Rotating a Deque
print("\n--- 5. ROTATING A DEQUE ---")

# Rotate right (positive steps) - O(k)
dq.rotate(2)  
print(f"Deque after rotate(2): {dq}")

# Rotate left (negative steps) - O(k)
dq.rotate(-3)
print(f"Deque after rotate(-3): {dq}")


# 6. Checking Size and Clearing a Deque
print("\n--- 6. SIZE AND CLEAR ---")

# Length of deque - O(1)
print(f"Length of deque: {len(dq)}")

# Clearing all elements - O(1)
dq.clear()
print(f"Deque after clear(): {dq}")

# 7. Deque vs List Performance
print("\n--- 7. DEQUE VS LIST PERFORMANCE ---")

"""
Deque Advantages Over List:
- O(1) time complexity for append and pop operations from both ends.
- Lists require O(n) for insertions/deletions at the beginning.
- Deques provide fast access for queue-based operations.

List Advantages Over Deque:
- Lists provide O(1) index access, while deque has O(n) access.
"""

# 8. Time Complexity Summary
print("\n--- 8. TIME COMPLEXITY SUMMARY ---")
print("Operation                               | Time Complexity")
print("---------------------------------------- | ----------------")
print("Append (dq.append(x))                   | O(1)")
print("Append Left (dq.appendleft(x))          | O(1)")
print("Pop (dq.pop())                          | O(1)")
print("Pop Left (dq.popleft())                 | O(1)")
print("Extend (dq.extend(iterable))            | O(k)")
print("Extend Left (dq.extendleft(iterable))   | O(k)")
print("Remove (dq.remove(value))               | O(n)")
print("Index Access (dq[i])                    | O(n)")
print("Rotate (dq.rotate(k))                    | O(k)")
print("Clear (dq.clear())                       | O(1)")
print("Check Length (len(dq))                   | O(1)")

print("\nThis guide covers the key functionalities and performance characteristics of deque.")