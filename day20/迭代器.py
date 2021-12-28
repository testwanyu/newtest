with open(r'D:\day19\day20\diedaiqi.txt',mode='r',encoding='utf8') as f:
    try:
        while True:
            line = next(f)
            print(line,end='')
    except StopIteration as e:
        print(e)


with open(r'C:\Users\Administrator\Desktop\diedaiqi.txt',mode='r',encoding='utf8') as fw:
    try:
        while True:
            line = next(fw)
            print(line,end='')
    except Exception as e:
            print(e)



items = [1,2,3]
# Get the iterator
it = iter(items)  #Invokes items._iter_()
#Run the iterator
print(next(it))      #Invokes it._next_()
print(next(it))
print(next(it))


for i in range(0,4,1):
    print(i)

def frange(a,b,c):
    x = a
    while x < b:
        yield x
        x+=c
for i in frange(0,4,0.5):
    print(i)
res1 = list(frange(0,4,0.125))
print(res1)

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
"""
到这里你可能就明白yield和return的关系和区别了，带yield的函数是一个生成器，而不是一个函数了，这个生成器有一个函数就是next函数，
next就相当于“下一步”生成哪个数，这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从
foo函数的开始执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束。
————————————————
版权声明：本文为CSDN博主「冯爽朗」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/mieleizhi0522/article/details/82142856/
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Test():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return  '这个类的名字是: % s' % self.name

print(Test('科学'))
