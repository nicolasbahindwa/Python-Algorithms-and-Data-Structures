"""
How it works:

Start from the first element and compare it with the target value
If they match, return the index
If not, move to the next element
Repeat until either the element is found or the end of the array is reached

Time Complexity:

Best case: O(1) - when the target is the first element
Worst case: O(n) - when the target is the last element or not present
Average case: O(n/2) ≈ O(n)

Binary Search
Binary search is a more efficient algorith"""

# Example array (must be sorted for binary search)
arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
target = 23

for i in arr:
    if i == target:
        print(i)


for i in range(len(arr)):
    if arr[i] == target:
        print(i) # printing the index of the targer it is found


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(i)
            return -1
    return -1
    

