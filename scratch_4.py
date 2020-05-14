
# Decorators

def div(a, b):
    print(a / b)


def smart_div(func1):
    def inner(a1, b1):
        if a1 < b1:
            a1, b1 = b1, a1
        return func1(a1, b1)
    return inner

div = smart_div(div)


div(2, 4)
