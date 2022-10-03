def mul(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


arr = []
n = int(input())
for i in range(n):
    tmp = int(input())
    arr.append(tmp)
print(mul(arr))
