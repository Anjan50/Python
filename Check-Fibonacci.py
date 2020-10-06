import math 
  
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
 
def isFibonacci(n): 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
x = int(input("Enter a number :"))
if (isFibonacci(x) == True): 
    print(x,"is a Fibonacci Number")
else: 
    print(x,"is a not Fibonacci Number ")