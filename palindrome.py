#!/usr/bin/env python3
# check if a word is a is_palindrome or not (Case-sensitive)
from math import floor
from sys import argv

def is_palindrome(word):
    length = len(word)
    if length < 2:
        return True
    max_check_position = floor(length / 2) + length % 2
    # print("max_check_position", max_check_position)
    for i in range(0, max_check_position + 1):
        backwards = word[length - 1 - i]
        # print("i", i)
        # print("stop_at", backwards)
        if word[i] != backwards and max_check_position >= 0:
            return False
    return True

if __name__ == "__main__":
    word = argv[1]
    if is_palindrome(word):
        print("'{}' is a palindrome".format(word))
    else:
        print("'{}' is not a palindrome".format(word))