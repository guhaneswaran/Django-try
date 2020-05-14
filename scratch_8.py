# Methods:

# Instance method , class method , static method

# Instance method  - two types Accessor method and Mutator method

# Accessor method - Just fetch the value of instance variable
# Mutator method - Change the value of the instance variable

class Student:

    school = 'Telusko' # Class variable

    def __init__(self , m1, m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): # instance method as it works with the object
        return ( self.m1 + self.m2 + self.m3)/3

    # CAN USE GETTERS AND SETTERS
    def get_m1(self): # GETTERS - only gets the value and doesnt change hence Accessor
        return self.m1

    def set_m1(self , value): # we can use constructors to pass the value or setters
        self.m1 = value # SETTERS -  change the values hence Mutators

    @classmethod # This is a decorator used for class method
    def getSchool(cls): # working with class variable we use cls. This is a CLASS METHOD
        return cls.school

    @staticmethod # This is a decorator used for static method
    def info(): # This is static method. Doing something extra notthing to do with class or instance
        print("This is a Student class ...")



s1 = Student(34, 65, 77)
s2 = Student(23, 65 , 12)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())

Student.info()