# '#' is used for single line and multiline comment
# ''' triple quotes for documentation

from functools import reduce

from numpy import *

arr = array([1, 2, 3, 4, 5])

print(arr)

lis = [1, 2, 3, 4, 5]  # stores elements

print(type(lis))

tup = (1, 2, 3, 1, 5)
print(tup)

print(tup.count(1))  # returns the no of times 1 comes in the tuple

s = {22, 23, 45, 32, 45}
print(s, type(s))  # output ll be in different sequence {32, 45, 22, 23} with the duplicates removed ,
# hence set cannot be accessed using indexes as SET uses HASHES to store and retrieve data

dicti = {1: 'Navin', 4: 'Harsh'}

print(dicti, type(dicti))

print(dicti[4])

print(dicti.keys(), dicti.values(), dicti.get(1), dicti.get(2), dicti.get(2, 'Not Found'))

keys = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'Go']

data = dict(zip(keys, values))  # first we have to zip key and values and then convert ZIP into dictionary

data['Mounkia'] = 'C#'

print(data)

del data['Kiran']

print(data)

prog = {'JS': 'Atom', 'C#': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'NetBeans', 'JEE': 'Eclipse'}}

print(type(prog), prog['Java']['JEE'])

num = 5
print(id(num))  # o/p 140709334082512

num1 = num

print(id(num1))  # will be same as address of num o/p 140709334082512

num2 = 5

print(id(num2))  # will be same as address of num or num1 coz address is based on the value o/p 140709334082512

num2 = 10

print(id(num2))  # Address will change o/p 140709334082672

PI = 3.14

# a = input("Enter a number") # By default input() returns string . Hence, here we have to typecase to int
# a = int(input("Enter a number"))

# x = input("Enter a character")[0] # This will take only one character even if the user inputs a string

res = eval('2+3')
print(res)

arr = array([1, 2, 3, 4, 5])

print("arr  ", arr)

# divides the range into 5 outputs . 0 start of range, 14 - end of range , 5 - factor
arr1 = linspace(0, 14, 5)  # [ 0.   3.5  7.  10.5 14. ]

print(arr1)

arr3 = logspace(1, 40, 5)  # [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30 1.00000000e+40]

print(arr3)

# same as range 1 -> start, 14 -> end , 2 is the range increment count
arr2 = arange(1, 14, 2)  # [ 1  3  5  7  9 11 13]

print(arr2)

# Create an array with all zeros of length 5 . By default - FLOAT
arr4 = zeros(5)

print(arr4)  # [0. 0. 0. 0. 0.]

arr4_1 = zeros(5, int)
print(arr4_1)  # [0 0 0 0 0]

# Create an array with all one's of length 5
arr5 = ones(5)  # [1. 1. 1. 1. 1.]

print(arr5)

arr6 = array([1, 2, 3, 4, 5])

arr6 = arr6 + 2  # adds 2 to each element in array

print(arr6)

arr7 = array([1, 2, 3, 4, 5])

arr8 = arr6 + arr7  # called as vectorized operation . ADDING TWO ARRAYS

print("Added array", arr8)

# to find SIN of an array

print(sin(arr8))

# to find sum, min , max , sort, concatenate of array
print(min(arr8), sum(arr8), sort(arr8), concatenate([arr6, arr7]))  # 4 40 [ 4  6  8 10 12] [3 4 5 6 7 1 2 3 4 5]

# Copying arrays

arr9 = arr8  # this copies the array but both the arrays will have same location. Called as ALIASING

print(arr9, arr8, id(arr9), id(arr8))  # [ 4  6  8 10 12] [ 4  6  8 10 12] 1897971084944 1897971084944

arr10 = arr8.view()  # copies array and it will have different location . This is called SHALLOW COPY
# when any value inside arr8 is changed , arr10 will also get changed

print(arr10, arr8, id(arr10), id(arr8))  # [ 4  6  8 10 12] [ 4  6  8 10 12] 2705141096320 2705141096000

arr11 = arr8.copy()  # This is called DEEP COPY
# when any value inside arr8 is changed , arr10 will not get changed

arr12 = array([[1, 2, 3], [4, 5, 6]])

# dtype prints the type if array elements , ndim - the dimension of the array , shape - gives no. of rows n colmns
print(arr12, arr12.dtype, arr12.ndim, arr12.shape)  # [[1 2 3]
# [4 5 6]] int32 2 (2, 3)
# Convert 2D into 1D array
arr13 = arr12.flatten()

print(arr13)  # [1 2 3 4 5 6]

arr8 = append(arr8, [20])

print(arr8)

# Converts 1D to 2D array reshape(rows, columns)
arr14 = arr8.reshape(2, 3)

print(arr14)

arr8 = append(arr8, [24, 29])

# converts 1D to 3D
arr15 = arr8.reshape(2, 2, 2)
print("3D Array ", arr15)

# Matrices
# convert 2D array into Matrix
print(matrix(arr14))


# Functions
def greet():
    print("Hello")
    return "Hey"


print(greet())


# in python we dont use both CALL by VALUE and REFERENCE
# integer and string are immutable
# lists are mutable
def update(x):
    print(id(x))  # 140709772715120
    x = 8
    print("Inside fn ", x, id(x))  # Inside fn  8 140709772715056


a = 10
update(a)
print("Outside fn ", a, id(a))  # Outside fn  10 140709772715120

lst = [2, 3, 4]


def update_lst(x):
    print(id(x))  # 2641693629000
    x[1] = 6
    print(x, id(x))  # [2, 6, 4] 2641693629000


print("id of lst outside", id(lst))  # id of lst outside 2641693629000
update_lst(lst)
print("id of lst outside - after fn call", id(lst), lst)  # id of lst outside - after fn call 2641693629000


# here b can take any no of arguments as tuple
def sum(a, *b):
    print("a ", a, "b ", b)  # a  3 b  (4, 6)


sum(3, 4, 6)  # if sum(2, 3) -> fn call , sum(*a) is fun defn, then a will be a tuple having 2 and 3


# Keyworded variable length arguments

def person(name, **data):  # Here we want Name as a must parameter . but the rest all arguments depends on what the
    # user needs. Hence, we need to use ** instead of * in the second argument. Acts like a
    # Dictionary
    print(name)
    print(data)

    for i, j in data.items():  # Can use like this to print the key-value pairs
        print(i, j)


person('Navin', age=26, city='Mysore', phone=123456)

# use global variable inside a function

gv = 10
gv_1 = 10
print(id(gv_1))


def something():
    global gv  # using the gv as global variable. So whatever we do with gv inside this fn .. it ll impact global
    print(gv)
    gv = 15  # changes the global variable


something()
print(gv)


# this is a better way
def something_1():
    gv_1 = 9

    x = globals()['gv_1']
    print(id(x), gv_1, x)

    globals()['gv_1'] = 15
    print(globals()['gv_1'], x)
    print(" Global values {}".format(globals()['gv_1']))


something_1()

# lambda or Anonymous functions:

# lambda is used when only a single expression needs to be evaluated

fn = lambda a: a * a

result = fn(5)
print(result)

# Filter Map Reduce

# reduce alone belongs to functools import statement. Filter and Map is available by default

# Filter - To filter the content in the iterable . Here iterable means list , etc
# Map - To change every value in the iterable, we can use MAP
# Reduce - to add all values, mulltiply all values, etc

nums = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(filter(lambda n: n % 2 == 0, nums))

print(evens)

doubles = list(map(lambda n: n * 2, nums))

print(doubles)

sum = reduce(lambda a, b: a + b, nums)

print(sum)

# Iterator

numb = [7, 8, 9, 10]

print(numb[2])

for i in numb:
    print(i)

itr = iter(numb)

print(itr.__next__())
print(itr.__next__())
print(itr.__next__())
 # OR below
print(next(itr))
