import string

abc = string.ascii_uppercase


def caesar(txt, n, coded=False):
    """ returns the coded or decoded text """
    result = ""
    for char in txt.upper():
        if char not in abc:
            result += char
        elif coded:
            result += abc[(abc.find(char) + n) % len(abc)]
        else:
            result += abc[(abc.find(char) - n) % len(abc)]
    return result


n = 3
x = caesar("Hello, here I am!", n)
print(x)
print(caesar(x, n, True))
