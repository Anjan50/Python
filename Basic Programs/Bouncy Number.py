'''
A number is said to Bouncy number if the digits of the number are unsorted.

For example,
22344 - It is not a Bouncy number because the digits are sorted in ascending order.
774410 - It is not a Bouncy number because the digits are sorted in descending order.
155349 - It is a Bouncy number because the digits are unsorted.
A number below 100 can never be a Bouncy number.

Write a program in Python to accept a number. Check and display whether it is a Bouncy number or not.
'''

#Function Starts-----------------------------
def isBouncy(num : int)-> bool:
	
	if num < 100:
		return False
	
	h = 0
	for i in str(num):
		i = int(i)
		if h > i:
			return False
		h = i
		#h Becomes Storage For Prev Digit
	return True
#Function Ends-------------------------------

num = int(input("Enter Number To Check:"))
if isBouncy(num):
	print(f"Given Number {num} Is A Bouncy Number.")
else:
	print(f"Given Number {num} Is Not A Bouncy Number.")

