#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
函数式编程
纯粹的函数式编程语言编写的函数没有变量
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

高阶函数
        map
        reduce
        filter
        sorted
闭包 (函数作为返回值时注意)
lambda 匿名函数
Decorator 装饰器 (见 Decorator.py )
偏函数
'''

# 高阶函数
print abs(-10)
print abs
# 函数本身也可以赋值给变量
f = abs
print f
print 'f:',f(-10)

# abs = 10
# print abs
# 由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。

'''
高阶函数: 一个函数就可以接收另一个函数作为参数
'''
def add(x, y, f):
    return f(x) + f(y)

print add(-5, 6, abs)

'''
map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
'''
def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def Name(l):    
    def upperFirstLetter(s):
        if not isinstance(s, str):
            raise TypeError('s is not str')
        if len(s) > 0:
            s = s.lower()
            if len(s) == 1:
                return s.upper()
            else:
                return s[0].upper() + s[1:]
        return s
    return map(upperFirstLetter, l)

print Name(['adam', 'LISA', 'barT'])

'''
reduce把一个函数作用在一个序列[x1, x2, x3...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
def add2(x, y):
    return x + y
print reduce(add2, [1, 3, 5, 7, 9])

def fn(x, y):
    return x * 10 + y

print reduce(fn, [1, 3, 5, 7, 9])

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '13579'))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print 'str2int:',str2int('13579')

# lambda
def str2int2(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

print 'str2int2:',str2int2('13579')

# 接受一个list并利用reduce()求积
def prod(l):
    def chen(x,y):
        return x * y
    return reduce(chen, l)

print 'prod:',prod([1,2,3,4,5]) 

'''
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
'''
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])    # [1, 5, 9, 15]


def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])    # ['A', 'B', 'C']

# 1~100的素数
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False 
    return True

print filter(is_prime,range(100))

print 10 ** 0.5     # 10e0.5

'''
sorted 排序算法
'''

print sorted([36, 5, 12, 9, 21])

# 倒序
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    else:
        return 0

print sorted([36, 5, 12, 9, 21], reversed_cmp)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，'Z' < 'a'
print sorted(['bob', 'about', 'Zoo', 'Credit'])

# 忽略大小写
def cmp_ignore_case(s1, s2):
    s1 = s1.upper()
    s2 = s2.upper()
    if s1 < s2:
        return -1
    if s1 > s2:
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)

'''
函数作为返回值
'''

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print calc_sum(0,1,2,3,4,5,6,7,8,9)         # 45
print calc_sum(*(0,1,2,3,4,5,6,7,8,9))      # 45
print calc_sum(*range(10))                  # 45


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

su = lazy_sum(*range(10))
print su        # <function sum at 0x000000000236B198>
print su()      # 45
# 每次调用都会返回一个新的函数，即使传入相同的参数
print lazy_sum(1, 3, 5, 7, 9) == lazy_sum(1, 3, 5, 7, 9)    # False

'''
闭包 (函数作为返回值时注意)
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量,解决办法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，已绑定到函数参数的值不变：
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1,f1()
print f2,f2()
print f3,f3()

def count2():
    fs = []
    for i in range(1, 4):
        def f(j):
            return lambda :j*j
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print f1,f1()
print f2,f2()
print f3,f3()


'''
lambda 匿名函数
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
'''
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
f = lambda x: x * x
print f,f(5)

def build(x, y):
    return lambda: x * x + y * y
f = build(2,3)
print f,f()

'''
偏函数
functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单
'''

# int()函数默认按十进制转换
print int('12345')              # 12345
print int('12345', base=8)      # 5349
print int('12345', 16)          # 74565

import functools
int2 = functools.partial(int, base=16)      # 设置默认值 base=16
print int2('12345')             # 74565
print int2('12345', base=8)     # 5349

# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10)
print max2(5, 6, 7)             # args = (10, 5, 6, 7)
