# Multi-threading
# By default , when we execute a program, it uses only one thread called 'MAIN Thread'

from threading import *
from time import sleep



class Hello(Thread):
    def run(self):  # This is a inbuilt method for executing thread
        for i in range(2):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(2):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()  # This will inturn execute 'run'
sleep(0.2)
t2.start()

print("Bye") # This is printed by Main thread

t1.join() # used to tell main thread to run after individual thread
t2.join()

print("Join Bye")


# File Handling

f = open('a1.txt' , 'r')

print(f , type(f))

#print(f.read(), end='#') # Prints the whole file
# print(f.readline(), end='#') # Print only one line
# print(f.readline(4) , end='#') # Prints only 1st 4 characters

f1 = open('a2.txt', 'w')

f1.write("Something")
f1.write("laptop") # This overwrites 'something'

f2 = open('a3.txt', 'a')

f1.write("Something")
f1.write("book")

for data in f:
    print(data)
    f2.write(data)


f3 = open('a4.jpg' , 'rb') # Reading image files since internally its binary , we use 'b'