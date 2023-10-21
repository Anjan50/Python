# Python Implementation for Interpolation Search Algorithm:

def interpolationSearch(arr, lo, hi, x):

    # The target must be in range defined by the corner:
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
        # Probing position(uniform distance):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
      
        # Target found:
        if arr[pos] == x:
            return pos
 
        # If target is larger, it's in right subarray:
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,hi, x)
 
        # If target is smaller, it's in left subarray:
        if arr[pos] > x:
            return interpolationSearch(arr, lo, pos - 1, x)
    return -1
 
# Array of sorted items:
arr = [10, 21, 35, 47, 52, 58, 76, 81, 92, 96]

# Element to be searched
target = 35
index = interpolationSearch(arr, 0, len(arr) - 1, target)

# Checking if the element is found or not:
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
