
# Operator Overloading
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        if ( self.m1 > other.m1):
            return True
        else:
            return False

    def __str__(self):
        return '{} {} '.format(self.m1 , self.m2) # usually it returns tuple


s1 = Student(46, 65)
s2 = Student(45, 65)

s3 = s1 + s2

print(s3.m1, s3.m2)

print( 1+2 )


if s1 > s2 :
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a) # same as print(a.__str__())
print(a.__str__())

print(a.__sizeof__())

print(s1.__str__())
