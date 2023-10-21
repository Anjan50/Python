def is_monotonic(array):
    increasing = decreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            decreasing = False
        elif array[i] < array[i - 1]:
            increasing = False

    return increasing or decreasing

# Example usage:
arr1 = [1, 2, 2, 3]
arr2 = [3, 2, 1]
arr3 = [1, 1, 1, 2, 3]
arr4 = [2,1,2,1,2]

if is_monotonic(arr1):
    print("arr1 is monotonic.")
else:
    print("arr1 is not monotonic.")

if is_monotonic(arr2):
    print("arr2 is monotonic.")
else:
    print("arr2 is not monotonic.")

if is_monotonic(arr3):
    print("arr3 is monotonic.")
else:
    print("arr3 is not monotonic.")

if is_monotonic(arr4):
    print("arr3 is monotonic.")
else:
    print("arr3 is not monotonic.")