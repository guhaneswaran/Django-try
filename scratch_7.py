# Instance variables - changes depends on the object. Defined inside __init__

# Class Variables  - is fixed. Defined outside __init__ inside the class

# Namespace- the space where we create and store object/variable

# Class namespace - to store all the class variable

# Instance namespace - to store all the instance variable




class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10 # Instance variables
        self.company = 'BMW' # Instance variables



c1 = Car()
c2 = Car()

c1.mil = 8 # Changing instance variable

print( c1.mil , c1.company , c1.wheels)
print( c2.mil , c2.company , c2.wheels)

Car.wheels = 5 # changing class variable

print( c1.mil , c1.company , c1.wheels)
print( c2.mil , c2.company , c2.wheels)