# Take 2 nos from user
number1 = float(input("First number: "))
number2 = float(input("\nSecond number: "))

#Display number before swap
print("Before swapping: a= {0} ,b= {1}".format(number1,number2))

# Swapping two numbers
number1 ,number2 = number2 ,number1

# Display number after swap
print("After swapping: a= {0} ,b= {1}".format(number1,number2))
