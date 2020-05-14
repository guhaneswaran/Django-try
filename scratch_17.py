# Generator. Generator will give iterator
# return terminates the function but yield still keeps track of the fn
# why using genetaror:
# ex .. fetching 1000 records from DB but we want to work with one value at a time. That time we can use Generator

def top10():
    yield 5
    yield 2
    yield 3
    yield 4


values = top10()

print(values.__next__())


for i in values: # for loop inturn uses iter and next
    print(i)


# Print all the perfect square

def sqr():
    n = 1

    while n<=10:
        sq = n*n
        yield sq
        n+=1

values = sqr()

for i in values:
    print(i)
