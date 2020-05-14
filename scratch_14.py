# We don't have Method Overloading concept in Python. hence we have to use the concept of Variable length arguments,
# or Default arguments
#
# Only supports Method Overriding

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a, b ):
        s = a + b
        return s


s1 = Student(45, 65)

print(s1.sum(5, 9))


class A:

    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")


a1 = B()
a1.show()
