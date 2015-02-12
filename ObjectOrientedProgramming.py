#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
面向过程的程序
面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

OOP 面向对象编程
面向对象的程序设计把计算机程序视为一组对象的集合，
而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。
三大特点:
                        数据封装、继承和多态
'''

# 面向过程的程序
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    return '%s: %s' % (std['name'], std['score'])

print print_score(std1)
print print_score(std2)

# OOP 面向对象编程
# (object)表示该类是从哪个类继承下来的. object类，这是所有类最终都会继承的类
class Student(object):  

    '''
    Constructor
    '''
    def __init__(self, name, score):
        self.name = name
        self.score = score

    '''
            和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
    '''
    def print_score(self):
        return '%s: %s' % (self.name, self.score)
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)  # 创建Student的实例，创建实例是通过类名+()实现的
lisa = Student('Lisa Simpson', 87)
print '函数',print_score,'类',Student,'实例',bart
print bart.print_score(),bart.get_grade()
print lisa.print_score(),lisa.get_grade()


'''
和静态语言不同，Python允许对实例变量绑定任何数据。
也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
'''
bart.age = 8
print bart.age
# AttributeError: 'Student' object has no attribute 'age'
# print lisa.age 


'''
访问限制
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
'''
class Student2(object):
    
    '''
            在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
            特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
    '''

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    # 在方法中，可以对参数做检查，避免传入无效的参数
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

bart = Student2('Bart Simpson', 70)

# AttributeError: 'Student' object has no attribute '__name'
# print bart.__name
bart.set_score(80)
print bart.get_score()
# bart.set_score(101)           # ValueError: bad score

'''
Python解释器对外把__name变量改成了_Student__name
不同版本的Python解释器可能会把__name改成不同的变量名
'''
# AttributeError: 'Student2' object has no attribute '__name'
# print bart.__name             
print bart._Student2__name      # Bart Simpson


'''
继承
            可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；
多态
            在调用类实例方法的时候，尽量把变量视作父类类型，这样，所有子类类型都可以正常被接收；
'''
class Animal(object):
    def run(self):
        print 'Animal is running...'

# 继承
class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()

class Dog2(Animal):
    # 多态
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'


a = list()      # a是list类型
b = Animal()    # b是Animal类型
c = Dog()       # c是Dog类型

print isinstance(a, list)           # True
print isinstance(b, Animal)         # True
print isinstance(c, Dog)            # True

print isinstance(c, Animal)         # True
b = Animal()
print isinstance(b, Dog)            # False

'''
多态真正的威力：调用方只管调用，不管细节，
而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。

“开闭”原则
                    对扩展开放：允许新增Animal子类；
                    对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
'''
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog2())


'''
获取对象信息
'''
# 基本类型
print type(123)         # <type 'int'>
print type('str')       # <type 'str'>
print type(None)        # <type 'NoneType'>

# 函数或者类
print type(abs)         # <type 'builtin_function_or_method'>
print type(a)           # <type 'list'>
print type(b)           # <class '__main__.Animal'>

print type(123)==type(456)          # True
print type('abc')==type('123')      # True
print type('abc')==type(123)        # False

import types
print type('abc')==types.StringType         # True
print type(u'abc')==types.UnicodeType       # True
print type([])==types.ListType              # True
print type(str)==types.TypeType             # True

# 有一种类型就叫TypeType，所有类型本身的类型就是TypeType
print type(int)==type(str)==types.TypeType  # True

'''
isinstance()
'''
# object -> Animal -> Dog -> Husky
class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print 'isinstance(h, Husky)',isinstance(h, Husky)   # True
print 'isinstance(h, Dog)',isinstance(h, Dog)       # True

print type(h)           # <class '__main__.Husky'>

print isinstance('a', str)                          # True
print isinstance('a', (str, unicode))               # True
print isinstance(u'a', (str, unicode))              # True
# 由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：
print isinstance(u'a', basestring)                  # True


'''
dir()
获得一个对象的所有属性和方法
'''
print dir('ABC')
'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
'''
print len('ABC')
print 'ABC'.__len__()

# 我们自己写的类，如果也想用len()的话，就自己写一个__len__()方法
class Dog3(Animal):
    def __len__(self):
        return 100

d = Dog3()
print len(d)



class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

# 可以测试该对象的属性:
print hasattr(obj, 'x')         # 有属性'x'吗？    True
print obj.x

print hasattr(obj, 'y')         # 有属性'y'吗？    False
setattr(obj, 'y', 19)           # 设置一个属性'y'
print hasattr(obj, 'y')         # 有属性'y'吗？    True
print obj.y                     # 19
print getattr(obj, 'y')         # 获取属性'y'    19


#getattr(obj, 'z')              # AttributeError: 'MyObject' object has no attribute 'z'
print getattr(obj, 'z', 404)    # 获取属性'z'，如果不存在，返回默认值404


# 可以获得对象的方法：
print hasattr(obj, 'power')     # 有属性'power'吗？    True
fn = getattr(obj, 'power')      # 获取属性'power'并赋值到变量fn
print fn

print fn()                      # 调用fn()与调用obj.power()是一样的

'''
在Python这类动态语言中，有read()方法，不代表该fp对象就是一个文件流，
它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''
def readData(fp):
    pass

def readImage(fp):
    '''
            获取对象信息 的使用场景
           假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
           如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场
    '''
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
