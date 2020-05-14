# Size of object depends on size of the variables. This size is calculated by constructors __init__

class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self , other): # here c1 is self and c2 is other
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

print(id(c1))  # 2040239235872
print(id(c2))  # 2040239235928

print(c1.name)

c1.update()

print(c1.age, c2.age)

if c1.compare(c2):
    print("Objects are same")
else:
    print("Objects are Different")
