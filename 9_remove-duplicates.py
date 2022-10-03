from collections import OrderedDict


# Function to remove all duplicates from string and order does not matter
def removeDupWithoutOrder(str):
    return "".join(set(str))


# Function to remove all duplicates from string and keep the order of characters same
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))


if __name__ == "__main__":
    #string in which vowels need to be counted . Can be edited
    str = "Hackoctoberfest"
    print "Without Order = ", removeDupWithoutOrder(str)
    print "With Order = ", removeDupWithOrder(str)
