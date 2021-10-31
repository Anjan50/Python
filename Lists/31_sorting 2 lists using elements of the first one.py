# Sort the values of first list using second list

# taking 2 lists
list_one = [2,3,1,0]
list_two = [6,5,3,4]

# combining them together as tuples in a list
l = []
for i in range(len(list_one)):
    x = (list_one[i],list_two[i])
    l.append(x)
    
# sorting by the elements of the first list
l.sort()

list_one.clear()
list_two.clear()

# printing the result
for i in range(len(l)):
    list_one.append(l[i][0])
    list_two.append(l[i][1])
    
# output
print(list_one)
print(list_two)