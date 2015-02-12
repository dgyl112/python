#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
装饰器
例如在函数调用前后自动打印日志，但又不希望修改函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
decorator就是一个返回函数的高阶函数。
'''
def now():
    return '2013-12-25'

f = now
print f()
print 'now.__name__',now.__name__
print 'f.__name__',f.__name__

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

# 把@log放到now2()函数的定义处，相当于执行了语句：now = log(now)
@log
def now2():
    return '2014-01-15'

print now2.__name__,now2()

def log3(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)
@log3('execute')
def now3():
    return '2013-12-25'

print now3,now3()                   # <function wrapper at 0x000000000226FC88> execute now3():...
print 'now3.__name__',now3.__name__ # __name__已经从原来的'now'变成了'wrapper'

'''
Python内置的functools.wraps作用就是把原始函数的__name__等属性复制到wrapper()函数
'''
import functools
def log4(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log4
def now4():
    return 'now4'

print now4.__name__,now4()      # __name__ 仍然为now4

def log5(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log5('execute')
def now5():
    return 'now5'

print now5.__name__,now5()      # __name__ 仍然为now5

def log6(text = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log6()         # @log6 不可以直接写成这样
def now6():
    return 'now6'

@log6('execute')
def now7():
    return 'now7'

print now6()
print now7()






def f1(func):
    print "f1"
    rl = func()
    print rl
    return rl + "f1"

# f2 = f1(f2(arg = ""))
@f1
def f2(arg = ""):
    print "f2"
    return arg + "f2r"

print f2
#print f2("1") 出错
#print f1(None) 出错