def swap_case(s):
    up = ''
    for letter in s:
        if(letter.isupper()):
            up += letter.lower()     
        else:
            up += letter.upper()
    return up
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)