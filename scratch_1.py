# swap two variables without using third variable

a = 5
b = 7

a = a + b # 12
b = a - b # 5
a = a - b # 7

 # More efficient way is using XOR as 5 is 101 , 7 is 111 so 5+7 = 12 takes 4 bits which is expensive

a = a ^ b # 12
b = a ^ b # 5
a = a ^ b # 7

# more efficient way

a,b = b,a # here variables in right of = is resolved first , uses the concept of rotation