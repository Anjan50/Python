list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

pairs = zip(list2, list1)
z = [x for _, x in sorted(pairs)]
print(z)
