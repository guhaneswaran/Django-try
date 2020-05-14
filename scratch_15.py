# By default Python doesnt support Abstract classes but we can use ABC module Abstract Base Classes

# what and why is Abstract class?
# Method having only declaration and not definition. Class having abstract methods r abstract classes
# We cant create an instance of Abstract class. But we have to implement all the methods of an abstract class
# otherwise we will get an error

# Designing an application in OOPS way needs Abstract class concept. Abstract class is more like a blueprint
#


from abc import ABC, abstractmethod


class Computer(ABC):  # using abstract class

    @abstractmethod  # defining method as abstract
    def process(self):
        pass


class Laptop(Computer):
    def process(self): # Implementing absrtact method here
        print("its running")


com1 = Laptop()
com1.process()
