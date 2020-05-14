# Fibonacci series to get input from user and get the last fibonacci no or the same no. if it is fibonacci


def fib(n):  # 0 1 1 2 3 5 8 13 21
    #    print(n)
    a, b, c = 0, 1, 0

    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        while (c <= n):
            c = a + b
            a = b
            b = c

        print(a)


fib(int(input("Enter the number ")))


