## importing the module
import itertools

## initializing a string
string = input()

## itertools.permutations method
permutation_list = list(itertools.permutations(string))

## converting the tuples to string using 'join' method
for tup in permutation_list:
    print("".join(tup))
