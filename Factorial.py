n = int(input("Enter the number: "))
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 
      
print ("The factorial of {0} is : {1}".format(n, fact))