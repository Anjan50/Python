def money(m) :
    count = 0
    coin = [10, 5, 1]
    for i in coin :
        count += m // i
        m = m % i
    return count

print('Enter desired amount : ' , end = '')
m = int(input())
print(money(m))

