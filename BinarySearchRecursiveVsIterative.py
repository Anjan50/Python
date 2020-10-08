# recursive and iterative binary search

items = [1, 2, 3, 4, 5]

def binary_search_recursive(elements, target, low=0, high=len(items)-1):
  mid = (low + high) // 2
  if low > high: # terminating case 1: not found
    return -1 # not found status code
  elif elements[mid] == target: # terminating case 2: found
    return mid # index
  elif target < elements[mid]: # recursive case 1: search left half
    return binary_search_recursive(elements, target, low, mid-1)
  else: # target > elements[mid] # recursive case 2: search right half
    return binary_search_recursive(elements, target, mid+1, high)

def binary_search_iterative(elements, target):
    low = 0
    high = len(elements) - 1
    while low <= high: # valid bounds
        mid = (low + high) // 2
        if elements[mid] == target: # found
            return mid
        elif target < elements[mid]: # search left half
            high = mid - 1
        else: # target > elements[mid], search right half
            low = mid + 1
    return -1 # invalid bounds: not found

# main
print(binary_search_recursive(items, 2)) # successful search
print(binary_search_recursive(items, 8)) # unsuccessful search
print(binary_search_iterative(items, 2)) # successful search
print(binary_search_iterative(items, 8)) # unsuccessful search
