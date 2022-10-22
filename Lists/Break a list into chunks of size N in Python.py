def divide(l, n):
    for i in l:
        yield l[i:i + n]


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 6
x = list(divide(liste, n))
print(x)
