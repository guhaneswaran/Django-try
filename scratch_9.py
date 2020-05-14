# Inner class

class Student:

    def __init__(self, name, roll , brand , cpu , ram):
        self.name = name
        self.roll = roll
        self.lap = self.laptop(brand, cpu , ram)
        print("Inside main class constructor")

    def show(self):
        print("Inside main class " , self.name, self.roll)

    class laptop:

        def __init__(self, brand , cpu , ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
            print("Inside sub class constructor")

        def show(self):
            print("Inside sub class " , self.brand , self.ram , self.cpu)


s1 = Student('Navin', 2 , 'HP' , 'i5' , 12)
#s2 = Student('Jenny', 3)

s1.show()
#s2.show()

#print(s1.lap.brand)

lap1 = s1.lap
#lap2 = s2.lap

#print(id(lap1))  # 2092221558456

#print(id(lap2))  # 2092221558568

print(s1.lap.show())
#print(lap1.show())
