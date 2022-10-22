def count(n):
    c = 0
    while (n != 0):
        c = c + 1
        n = n // 10
    return (c)


def armst(n, a):
    if n == 0:
        return n
    else:
        return ((n % 10)**a + armst(n // 10, a))


x = int(input("Enter the 1st number:"))
y = int(input("Enter the 2nd number:"))
print("Armstrong numbers in the interval", (x, y), "=")
for i in range(x, y + 1):
    m = i
    a = count(i)
    p = armst(i, a)
    if m == p:
        print(m)
