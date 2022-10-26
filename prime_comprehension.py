"""
Programs retrieves prime number in list using comprehension technique for give n
"""

N=20
result = [  x for x in range(2, N)
            if all(x % y != 0 for y in range(2, x))
        ]
print(result)