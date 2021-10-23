input = input('')
sum1=0
for a in input:
    sum1+=ord(a)
print(sum1)
# It can also be written as:
print(sum([ord(a) for a in input]))
