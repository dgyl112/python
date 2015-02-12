#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
metaclass 元类
先定义metaclass，就可以创建类，最后创建实例。
换句话说，你可以把类看成是metaclass创建出来的“实例”。
'''
# metaclass是创建类，所以必须从`type`类型派生：
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
class ListMetaclass(type):
    '''
    metaclass可以给我们自定义的MyList增加一个add方法
    __new__()方法接收到的参数依次是：
    1. 当前准备创建的类的对象:
    2. 类的名字；
    3. 类继承的父类集合；
    4. 类的方法集合。
    '''
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类

# 普通的list没有add()
l = list()
# l.add(1)            # AttributeError: 'list' object has no attribute 'add'

L = MyList()
L.add(1)
L.add(2)
L.add(3)
print L


'''
Simple ORM using metaclass

ORM (Object Relational Mapping)    
对象-关系映射: 关系数据库的一行映射为一个对象，也就是一个类对应一个表
要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
'''

__author__ = 'Michael Liao'

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings        # 保存属性和列的映射关系
        attrs['__table__'] = name               # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:
class User(Model):
    id = IntegerField('uid')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()


'''
类属性和实例属性
在我们编写的ORM中，ModelMetaclass会删除掉User类的所有类属性，目的就是避免造成混淆。
'''
class Student(object):
    name = 'Student--'

s = Student()           # 创建实例s
print(s.name)           # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)     # 这和调用Student.name是一样的
s.name = 'Michael'      # 给实例绑定name属性
print(s.name)           # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)     # 但是类属性并未消失，用Student.name仍然可以访问
del s.name              # 如果删除实例的name属性
print(s.name)           # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

# join
print ','.join(['1','2','3'])   # 1,2,3
print ','.join('abc')           # a,b,c