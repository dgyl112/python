#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
动态给实例绑定一个属性,方法
'''

class Student(object):
    pass

s = Student()
s.name = 'Michael'          # 动态给实例绑定一个属性
print s.name

def set_age(self, age):     # 定义一个函数作为实例方法
    self.age = age

'''
给一个实例绑定的方法，对另一个实例是不起作用的
'''
from types import MethodType
s.set_age = MethodType(set_age, s, Student)         # 给实例绑定一个方法
s.set_age(25)               # 调用实例方法
print s.age                 # 测试结果        

s2 = Student()              # 创建新的实例
#s2.set_age(25)             # AttributeError: 'Student' object has no attribute 'set_age'

'''
为了给所有实例都绑定方法，可以给class绑定方法
'''
def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)

s.set_score(100)
print s.score

s2.set_score(99)
print s2.score


'''
__slots__
Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性

__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用
子类中定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
'''

class Student2(object):
    __slots__ = ('name', 'age')         # 用tuple定义允许绑定的属性名称

s = Student2()          # 创建新的实例
s.name = 'Michael'      # 绑定属性'name'
s.age = 25              # 绑定属性'age'
#s.score = 99            # AttributeError: 'Student2' object has no attribute 'score'

# 父类的__slots__对继承的子类是不起作用
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
print g.score


'''
@property
Python内置的@property装饰器就是负责把一个方法变成属性调用
'''

# 可以检查参数，但略显复杂
class Student3(object):
    
    def __init__(self):
        self._score = 0

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student3()
s.set_score(60)             # ok!
print s.get_score()
# s.set_score(888)            # ValueError: score must between 0 ~ 100!


# 用 @property
class Student4(object):
    '''
    @property的实现比较复杂，我们先考察如何使用。
            把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，
            负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    '''

    def __init__(self):
        self._score = 0
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student4()
s.score = 49        # OK，实际转化为s.set_score(60)
print s.score       # OK，实际转化为s.get_score()
#s.score = 9999     # ValueError: score must between 0 ~ 100!


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student5(object):

    '''
    birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
    '''
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth




'''
多重继承
'''
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# Runnable和Flyable的功能
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 多重继承
class Dog2(Mammal, Runnable):
    pass

class Bat2(Mammal, Flyable):
    pass



'''
Mixin
Mixin: 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。

由于Python允许使用多重继承，因此，Mixin就是一种常见的设计。
这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
'''

'''
Mixin的目的就是给一个类增加多个功能，这样，在设计类的时候，
我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系。

Python自带的很多库也使用了Mixin。
举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，
这两种模型由ForkingMixin和ThreadingMixin提供。通过组合，我们就可以创造出合适的服务来。

比如，编写一个多进程模式的TCP服务，定义如下：

class MyTCPServer(TCPServer, ForkingMixin):
    pass
编写一个多线程模式的UDP服务，定义如下：

class MyUDPServer(UDPServer, ThreadingMixin):
    pass
如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixin：

class MyTCPServer(TCPServer, CoroutineMixin):
    pass
'''




'''
定制类
Python的class中还有许多像__len__()这样有特殊用途的函数，可以帮助我们定制类。
'''

'''
__str__
直接敲变量不用print，打印出来的实例还是 <__main__.Student7 object at 0x0000000002159BE0>
这是因为直接显示变量调用的不是__str__()，而是__repr__()，
两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
也就是说，__repr__()是为调试服务的。
'''
class Student7(object):
    def __init__(self, name):
        self.name = name

print Student7('Michael')       # <__main__.Student7 object at 0x0000000002159BE0>

class Student8(object):
    '''__str__()'''
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    
    # 通常__str__()和__repr__()代码都是一样的
    __repr__ = __str__

print Student8('Michael')       # Student object (name: Michael)

'''
__iter__    ==>    for ... in
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1       # 初始化两个计数器a，b

    def __iter__(self):
        return self                 # 实例本身就是迭代对象，故返回自己

    # 返回下一个值
    def next(self):
        self.a, self.b = self.b, self.a + self.b        # 计算下一个值
        if self.a > 100:         # 退出循环的条件
            raise StopIteration();
        return self.a               

for n in Fib():
    print n


'''
__getitem__    ==>    list[]
像list那样按照下标取出元素，需要实现__getitem__()方法
'''
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib2()
print 'f[0]',f[0]
print 'f[1]',f[1]
print 'f[2]',f[2]


class Fib3(object):
    '''
    list有个神奇的切片方法对于Fib2却报错
            原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
    '''
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib3()
print f[:5]         # [1, 1, 2, 3, 5]
print f[3:10]       # [3, 5, 8, 13, 21, 34, 55]
print f[3:10:2]     # 没有对step参数作处理,依然返回 [3, 5, 8, 13, 21, 34, 55]



'''
__getattr__
调用类的方法或属性时，如果不存在，就会报错 AttributeError,要避免这个错误，
除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
'''
class Student9(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99                   # 返回属性

s = Student9()
print s.name
print s.score


class Student10(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25           # 返回函数
        elif attr=='score':
            return lambda x:x
        # raise AttributeError('\'Student10\' object has no attribute \'%s\'' % attr)
        # 其它返回 None

s = Student10()
print s.age()
print s.score(10)
print s.abc                             # None


'''
__getattr__ 用途
利用完全动态的__getattr__，我们可以写出一个链式调用

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
http://api.server/user/friends
http://api.server/user/timeline/list
'''

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
        
    def __str__(self):
        return self._path
    
    def __call__(self,path):
        return Chain('%s/%s' % (self._path, path))
    


print Chain().status.user.timeline.list         # /status/user/timeline/list

'''
还有些REST API会把参数放到URL中，比如GitHub的API：
GET /users/:user/repos
调用时，需要把:user替换为实际用户名
'''
print Chain().users('michael').repos



'''
__call__        ==> instance()
定义一个__call__()方法，就可以直接对实例进行调用.

对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，
把函数看成对象，因为这两者之间本来就没啥根本的区别。
'''
class Student11(object):
    def __init__(self, name):
        self.name = name

    def __call__(self,age=18):
        return('My name is %s. age is %d.' % (self.name,age) )
        
s = Student11('Michael')
print s()
print s(20)

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print callable(Student())                   # False
print callable(Student11('Michael'))        # True

print callable(max)                         # True
print callable([1, 2, 3])                   # False
print callable(None)                        # False
print callable('123')                       # False


'''
type()
动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，
而h是一个实例，它的类型就是class Hello。
class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
'''
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

'''
当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
from hello import Hello
'''
h = Hello()
h.hello()
print(type(h))                          # <class '__main__.Hello'>
print Hello, (type(Hello))              # <class '__main__.Hello'> <type 'type'>


# 先定义函数
def fn(self, name='world'): 
    print('Hello, %s.' % name)
    
'''
通过type()函数创建出Hello2类
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''
# 创建Hello class
Hello2 = type('Hello2', (object,), dict(hello=fn)) 
print Hello2,(type(Hello2))             # <class '__main__.Hello2'> <type 'type'>
