# POLYMORPHISM

# Loose Coupling
# Dependency Injection
# Interface

# 4 ways of implementing Polymorphism
# Duck typing
# Operator Overloading
# Method Overloading
# Method Overriding




# Duck Typing. Here code() inside laptop changes according to the type of object provided
class Pycharm:

    def execute(self):
        print("Compiling and Running....")


class Myeditor:

    def execute(self):
        print("Autocorrect..")
        print("Compiling and Running....")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = Pycharm()
lap1 = Laptop()
lap1.code(ide)

ide1 = Myeditor()
lap2 = Laptop()
lap2.code(ide1)


# Operator Overloading

a = 'Hello'
b = 'World'

print(a + b) # behind the scene it actually does the below line __add__ . These methods are called as magic methods
print(str.__add__(a, b))