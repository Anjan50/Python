# Python program to print all negative numbers in a range

# define the starting and ending points
start = -5
end = 7

# list comprehension to print the negative numbers in the given range
answer = [i for i in range(start, end + 1) if i < 0]
print(answer)
