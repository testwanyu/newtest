import re

a = [1,2,3]
b = [2,3,4]
a.extend(b)
print(a)
print(a+b)

a= 10
def f():
    a= 5
f()
print(a)

a = {'1':1,'2':2}
theCopy = a
a['1'] = 5
sum = a['1'] + theCopy['1']
print(sum)

# x ="foo"
# y = 123
# print(x+y)

class A:
    def who(self):
        print('A', end='')
class B(A):
    def who(self):
        super().who()
        print('B', end='')
class C(A):
    def who(self):
        super().who()
        print('C', end='')
class D(B, C):
    def who(self):
        super().who()
        print('D', end='')
item = D()
item.who()

print('*'*50)

str1 = "Python‘s features"
str2 = re.match(r'(.*)on(.*?).*', str1, re.M | re.I)
print(str2.group(1))

import sys, os
import os
import time