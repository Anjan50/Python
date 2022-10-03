a = [3, 4, 5]
n = 3
k = 2
d = []
for j in a:
    d.append(j)
for i in range(n):
    b = i + k
    if (b) > n - 1:
        b = b - n
    d[b] = a[i]
print(d)
