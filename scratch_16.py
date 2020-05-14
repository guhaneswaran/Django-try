# iterator . User defined

class Top10:

    def __init__(self):
        self.num = 1

    def __iter__(self):  # gives the object of the iterator
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = Top10()

print(values.__next__())

for i in values:
    print(i)

