# Class

class Computer:
    # Attributes

    # Behaviour
    def __init__(self, cpu , ram): # used to initialize the variables ( same as constructor) called for every object creation
        print(" in __init__")
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print(" I5 with 16GB RAM and 1 TB HDD")
        print("Config is ", self.cpu , self.ram)




comp1 = Computer(" octacore" , "12 GB")

print(type(comp1)) # <class '__main__.Computer'>

Computer.config(comp1) # Classname.method(object)

#comp2 = Computer()

#Computer.config(comp2)

# OR another method

comp1.config()
#comp2.config()




