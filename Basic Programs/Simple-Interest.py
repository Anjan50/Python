def simple_interest(p, t, r):
    si = (p * t * r) / 100
    return si


p = int(input("Enter the principal: "))
r = float(input("Enter the rate: "))
t = int(input("Enter the time: "))

result = simple_interest(p, r, t)
print('The Simple Interest is', result)
