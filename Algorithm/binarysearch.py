"""How it works:

Find the middle element of the array
If the middle element equals the target, return its index
If the target is less than the middle element, repeat the search in the left half
If the target is greater than the middle element, repeat the search in the right half
Continue until the element is found or the search interval is empty

Time Complexity:

Best case: O(1) - when the target is the middle element
Worst case: O(log n) - when the target is near the ends or not present
Average case: O(log n)

Example Usage"""


arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 92]
target = 23

left = 0
right = len(arr) -1

while left <= right:
    mid = (left + right) //2
    
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] > target:
        left = mid + 1
    else:
        right = mid -1



def binary_search(arr, target):
    left = 0
    right = len(arr) -1 
    
    while left <= right:
        mid = (left + right ) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left + 1
        else:
            right -1