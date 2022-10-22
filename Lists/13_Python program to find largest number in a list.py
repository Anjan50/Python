from random import randint

# generate a list of 10 random numbers
mylist = [randint(1, 100) for i in range(10)]


# find max element using loop
def getMax1(list):
    m = list[0]
    for i in list:
        if m < i:
            m = i
    return m


# find max element using recusion
def getMax2(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], getMax2(list[1:]))


# use sort to find max element
def getMax3(list):
    list.sort()
    return list[-1]


print("List: ", mylist)
print("max element using max function: ", max(mylist))
print("max element using loop: ", getMax1(mylist))
print("max element using recusion: ", getMax2(mylist))
print("max element using sort: ", getMax3(mylist))
