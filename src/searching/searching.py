def linear_search(arr, target):
    # Your code here
    for el in arr:
        if el == target:
            return arr.index(el)
    return -1

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr)-1

    while end >= start:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif target > arr[middle]:
            start = middle + 1
        elif target < arr[middle]:
            end = middle - 1

    return -1  # not found
