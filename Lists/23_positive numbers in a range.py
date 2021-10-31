# Python program to print all positive numbers in a range

# define the starting and ending points
start = -5
end = 7

# list comprehension to print the positive numbers in the given range
answer = [i for i in range(start, end+1) if i >= 0 ]
print(answer)