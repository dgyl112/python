#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年1月9日

@author: lee
'''

print cmp(1, 2)
print cmp(1, 1)
print cmp(2, 1)

print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print unicode(100)
print bool(1)
print bool('')

a = abs
print a(-1)

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type for my_abs():')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-2)
# print my_abs('A')    # error


import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print 'x', x, 'y', y
# 函数可以同时返回多个值，但其实就是一个tuple
t = move(100, 100, 60, math.pi / 6)
print t

# 默认参数,必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5)
print power(5, 2)

# 变化大的参数放前面，变化小的参数放后面
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name, 'gender:', gender, 'age:', age, 'city:', city
    # 没有返回值会默认返回None
    
print enroll('Sarah', 'F')
print enroll('Adam', 'M', city='Tianjin')

# 默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L

print add_end([1, 2, 3])
print add_end([1, 2, 3])
print add_end()
print add_end()  # error
print add_end()

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end2([1, 2, 3])
print add_end2([1, 2, 3])
print add_end2()
print add_end2()
print add_end2()

# 可变参数
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2)
print calc()


nums = [1, 2, 3]
nums2 = (1, 2, 3)
print calc(nums[0], nums[1], nums[2]) # 不够友好
# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数
print 'list',calc(*nums)
print 'tuple',calc(*nums2)

# 关键字参数
def person(name, age, **kw):
    return 'name', name, 'age', age, 'other:', kw

print person('Michael', 30)
print person('Bob', 35, city='Beijing')
print person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, **kw)


# 必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1, 2)                      # 必选参数
func(1, 2, c=3)                 # 默认参数
func(1, 2, 3, 'a', 'b')         # 可变参数
func(1, 2, 3, 'a', 'b', x=99)   # 关键字参数

'''
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
'''
# 通过一个tuple和dict，你也可以调用该函数
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(50)  # 递归调用的次数最大999

# 尾递归优化：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact2(n):
    return fact_iter(1, 1, n)

def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)
'''
遗憾的是，大多数编程语言没有针对尾递归做优化，
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
所以，即使把上面的fact2(n)函数改成尾递归方式，也会导致栈溢出。
'''
print fact_iter(1, 1, 5)
