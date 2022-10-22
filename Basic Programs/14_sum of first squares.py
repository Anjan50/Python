# Python Program for Sum of squares of first n natural numbers


def sum_of_squares(n):
    l = [i**2 for i in range(1, n + 1)]
    return sum(l)


print("sum of squares of first n natural numbers")
for i in range(1, 101):
    print("n={}, sum={}".format(i, sum_of_squares(i)))
