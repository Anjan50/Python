def check_list(c, lst):

    if c in lst:
        return True
    return False


lst = [8, 9, 's', 'p', 'q', 2, 5, 9]

print('Enter the element you want to check')
n = input()

if check_list(n, lst):
    print("Element present in the list")
else:
    print("Element not present in the list")
