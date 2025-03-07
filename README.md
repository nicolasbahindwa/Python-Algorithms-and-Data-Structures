# 🚀 Python Algorithms and Data Structures

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-FF6F00?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMC41OSA0LjU5QzEwLjIxIDQuMjEgOS43IDQgOS4xNyA0SDRjLTEuMSAwLTIgLjktMiAydjE0YzAgMS4xLjkgMiAyIDJoMTZjMS4xIDAgMi0uOSAyLTJWOGMwLS41My0uMjEtMS4wNC0uNTktMS40MWwtNC01Yy0uMzctLjM4LS44OC0uNTktMS40MS0uNTloLTQuODNjLS41MyAwLTEuMDQuMjEtMS40MS41OWwtMyAzek0xNSAxNGMwIDEuMS0uOSAyLTIgMnMtMi0uOS0yLTIgLjktMiAyLTJzMiAuOSAyIDJ6bS00LTZWMTdjMCAgLjU1LS40NSAxLTEgMUg2Yy0uNTUgMC0xLS40NS0xLTFWOGMwLS41NS40NS0xIDEtMWg0YS41LjUgMCAwIDEgLjM1Ljg1TDguNDEgOWgxLjE3Yy41NSAwIDEgLjQ1IDEgMXY4eiI+PC9wYXRoPjwvc3ZnPg==)
![Data Structures](https://img.shields.io/badge/Data_Structures-00B4AB?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0yMiAxOHYtMkgyVjZoMjB2MmgtMnYxMEgyeiBNMjAgMThoLTZWOGg2djEwek0xMSA4SDV2MTBoNlY4eiI+PC9wYXRoPjwvc3ZnPg==)

</div>

## 📊 Big O Notation

Big O notation is used to measure the efficiency of an algorithm in terms of **time complexity** and **space complexity** as input size grows.

### Common Big O Complexities

#### 1. <span style="color:#4CAF50">O(1) - Constant Time</span>
The runtime does not depend on the input size.

```python
# Example: Accessing an element in an array
arr = [1, 2, 3, 4]
print(arr[2])  # Always takes the same time
```

#### 2. <span style="color:#2196F3">O(log n) - Logarithmic Time</span>
The runtime decreases as the input size grows.

```python
# Example: Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

#### 3. <span style="color:#03A9F4">O(n) - Linear Time</span>
Time grows proportionally to input size.

```python
# Example: Linear search
for num in arr:
    if num == target:
        print("Found!")
```

#### 4. <span style="color:#009688">O(n log n) - Linearithmic Time</span>
Common in efficient sorting algorithms.

```python
# Example: Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right
```

#### 5. <span style="color:#FF9800">O(n²) - Quadratic Time</span>
Nested loops cause time complexity to grow exponentially.

```python
# Example: Bubble Sort
for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

#### 6. <span style="color:#F44336">O(2ⁿ) - Exponential Time</span>
Algorithm performance doubles with each additional input size.

```python
# Example: Fibonacci (Recursive)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

#### 7. <span style="color:#9C27B0">O(n!) - Factorial Time</span>
Extremely slow for large inputs, common in brute-force problems.

```python
# Example: Generating all permutations
from itertools import permutations
perm = list(permutations([1, 2, 3]))
```

## 📈 Complexity Comparison Chart

<div align="center">
  
![Big O Complexity Chart](https://user-images.githubusercontent.com/68016025/169524478-0c9aeffd-e5b9-4bc9-b1a9-37723bfe27f8.png)

</div>

## 📋 Summary Table

| Big O Notation | Complexity Type | Example Algorithms | Performance |
|----------------|----------------|-------------------|-------------|
| O(1)           | Constant       | Array Access, Hash Table | 🟢 Excellent |
| O(log n)       | Logarithmic    | Binary Search, Heap Operations | 🟢 Very Good |
| O(n)           | Linear         | Linear Search, Single Iteration | 🟢 Good |
| O(n log n)     | Linearithmic   | Merge Sort, Quick Sort, Heap Sort | 🟡 Fair |
| O(n²)          | Quadratic      | Bubble Sort, Insertion Sort | 🟠 Poor |
| O(2ⁿ)          | Exponential    | Recursive Fibonacci, Tower of Hanoi | 🔴 Very Poor |
| O(n!)          | Factorial      | Permutations, Traveling Salesman | 🔴 Extremely Poor |

## 💡 When to Choose Which Algorithm?

- **O(1), O(log n), O(n)**: Use for large datasets
- **O(n log n)**: Acceptable for medium to large sorting operations
- **O(n²)**: Only use for small datasets
- **O(2ⁿ), O(n!)**: Avoid if possible, or use only for very small inputs

## 📚 Resources

- [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms-third-edition) by Thomas H. Cormen
- [Python Data Structures and Algorithms](https://www.packtpub.com/product/python-data-structures-and-algorithms/9781786467355) by Benjamin Baka
- [LeetCode](https://leetcode.com/) - Practice platform
- [HackerRank](https://www.hackerrank.com/) - Practice platform

---

- reference : https://www.youtube.com/watch?v=dqLHTK7RuIo&list=PLKYEe2WisBTFEr6laH5bR2J19j7sl5O8R&index=4
<div align="center">

Made with ❤️ for algorithm enthusiasts

</div>