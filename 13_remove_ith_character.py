# Python program for removing i-th indexed character from a string


# Removes character at index i
def remove(string, i):

    for j in range(len(string)):
        if j == i:
            string = string.replace(string[i], "", 1)
    return string


# Driver Code
if __name__ == '__main__':

    #You can enter the string of your choice
    string = "hackoctoberfest"

    # Remove nth index element.You can edit the element which is in range of(0,len(string)-1)
    i = 5

    # Print the new string
    print remove(string, i)
