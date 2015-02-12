#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
切片(Slice)
            print L[:3]
迭代(Iteration)
            isinstance('abc', Iterable) 可以使用 for in循环
列表生成式    List Comprehensions
            [x * x for x in range(1, 11)]
生成器（Generator）
            1. 把一个列表生成式的[]改成()，就创建了一个generator
            2. 函数变成generator，只需要把 return 改为 yield 就可以
'''
# 切片(Slice)
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[:]          # ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]        # ['Michael', 'Sarah', 'Tracy']
print L[:3]         # ['Michael', 'Sarah', 'Tracy']
print L[1:3]        # ['Sarah', 'Tracy']
print L[-2:]        # ['Bob', 'Jack']
print L[-2:-1]      # ['Bob']        记住倒数第一个元素的索引是-1

L = range(100)
# 前10个数
print L[:10]
# 前10个数，每3个取一个
print L[:10:3]
# 后10个数
print L[-10:]
# 前11-20个数
print L[10:20]
# 所有数，每5个取一个
print L[::5]
# tuple也可以用切片操作，只是操作的结果仍是tuple
t = (0, 1, 2, 3, 4, 5)
print t[:3]
s = 'ABCDEFG'
print s[:3]                 # ABC
print 'ABCDEFG'[::2]        # ACEG

# 迭代 Iteration
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key,d[key]
for value in d.itervalues():
    print value
for k, v in d.iteritems():
    print k,v
    
for ch in 'ABC':
    print ch

# 判断一个对象是否可迭代对象
from collections import Iterable
print isinstance('abc', Iterable)       # True    str是否可迭代
print isinstance([1,2,3], Iterable)     # True    list是否可迭代
print isinstance(123, Iterable)         # False   整数是否可迭代


# 对list实现类似Java那样的下标循环
# enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y


# 列表生成式    List Comprehensions
'''
Python内置的非常简单却强大的可以用来创建list的生成式
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
'''
print range(1, 11)
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]
# 两层循环，可以生成全排列 
print [m + n for m in 'ABC' for n in 'XYZ']
    
import os # 导入os模块
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录   
# 列表生成式也可以使用两个变量来生成list  
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]
# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
# 非字符串类型没有lower()方法
L = ['Hello', 'World', 18, 'Apple', None]
print [ s.lower() for s in L if isinstance(s, str)]

# 生成器（Generator）：     一边循环一边计算的机制
# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(20)[-10:]]
print L
g = (x * x for x in range(20)[-10:])
print g
for n in g:
    print n

# 斐波拉契数列（Fibonacci）
print 'Fibonacci:'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
fib(6)
print 'fib(6):',fib(6)    # 函数返回值 None
'''
一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
'''
# 把fib函数变成generator
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print 'fib2:',fib2
print 'fib2(6):',fib2(6)
'''
变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
print 'o:',o
print o.next()
print o.next()
print o.next()
# print o.next()    # 没有更多的元素时，抛出StopIteration的错误

# 基本上从来不会用next()来调用它，而是直接使用for循环来迭代
for n in fib2(6):
    print n
