# Program to print prime numbers till a number

def getPrimes(n):
    prime = [True for x in range(n)]
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n, p):
                prime[i] = False
        p += 1
    return prime


# Number used in this example is 50. You can replace it with any other number as required.
n = 50
primes = getPrimes(n)
print("The prime numbers less than "+str(n)+" are")
for i, j in enumerate(primes):
    if j and i > 1:
        print(i)
