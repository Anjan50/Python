# Python3 code to count vowel in a string using set


# Function to count vowel
def vowel_count(str):

    # Initializing count variable to 0
    count = 0

    # Creating a set of vowels
    vowel = set("aeiouAEIOU")

    # Loop to traverse the alphabet in the given string
    for alphabet in str:

        # If alphabet is present in set vowel
        if alphabet in vowel:
            count = count + 1

    print "No. of vowels :", count


#string in which vowels need to be counted . Can be edited
str = "Hackoctoberfest"
vowel_count(str)
