# recursion - FACTORIAL

import sys

print(sys.getrecursionlimit())  # by default the recursion limit is 1000

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


res = fact(5)

print(res)
