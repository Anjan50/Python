#Convert a Decimal Number to its Binary, Octal and Hexadecimal format
#Language- Python 3.8.5 64-bit
#Author- @PrithirajN

#Take the input
n = int(input("Enter a decimal number: "))

print('The binary format of {} is: {}'.format(n,bin(n).replace("0b", "")))
print('The octal format of {} is: {}'.format(n, oct(n).replace("0", "")))
print('The hexadecimal format of {} is: {}'.format(n, hex(n).replace("0x", "")))