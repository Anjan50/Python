"""
Reverse the given integer number without converting into str
"""
num = 123
rev = 0
while num:
    rem = num % 10
    rev = rev * 10 + rem
    num = num / 10

print("Reversed Number : ", rev)
