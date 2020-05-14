# Constructor in inheritance
# Lets say A is parent and B is child. when we invoke constructor of A only A's init is cald.
# Lets say only A has init and B doesnt,here if we invoke B ,since B doesnt have its won constructor, A's init is used
# If B has its own constructor, then B is init is only called and As init is ignored
# Inorder to call init for class A while invoking B , we have to use super().__init__ to invoke A's init

# Method Resolution Order


class A:  # Super class or Parent class

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):  # B is a child class of A or sub class

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


a1 = A()
b1 = B()

# in Multiple inheritance, lets say C takes from both A and B, and if we do super().__init__ in C, it can either call
# A or B's init. But it ll choose A because of MRO
# MRO always goes from left to Right. Hence here A's init will be chosen
#
