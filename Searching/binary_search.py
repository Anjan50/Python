def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
