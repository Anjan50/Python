#Reverse a given Number
#Language- Python 3.8.5 64-bit
#Author- @PrithirajN

def reverse(x):
    # get positive number irrespestive of the original sign
    if x > 0:
        n = x
    else:
        n = -x
    c = 0

    while n > 0:
        r = n % 10
        c = c*10 + r
        n = n // 10

    # reset value to 0 if answer exceeds the constraint
    if c > ((2**31)-1):
        c = 0

    # return the answer with the original sign
    if x > 0:
        print(c)
    else:
        print(- c)

reverse(1234)#Example
