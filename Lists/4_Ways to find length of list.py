l = list(range(10))

def length1(list):
    # find length of list using loop
    c = 0
    while list != []:
        list.pop()
        c += 1
    return c

def length2(list):
    if list == []:
        return 0
    else:
        return 1 + length2(list[1:]) # using recusion

# using len function to find length
print("Length of list using len function: ", len(l))

# using for loop to find length
print("Length of list using while loop: ", length1(l.copy())) # using copy to avoid changing original list

# using recusion to find length
print("Length of list using recusion: ", length2(l.copy())) # using copy to avoid changing original list

