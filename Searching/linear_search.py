def search(arr, x):
    for index, element in enumerate(arr):
        if element == x:
            return index
    return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
result = search(arr, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
