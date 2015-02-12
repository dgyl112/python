#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年1月8日

@author: lee
'''


#name = raw_input("输入名字：")
#print 'hello,', name

#a = int(raw_input("输入整数："))
#print a
    
# 用r表示内部的字符串默认不转义
print r'\\\t\\'
print "\\\t\\"
print r'''\\\t\\'''

print '''line1
line2
line3'''

print '3 > 2 is',3 > 2
print True
print False

print '运算符'
print True and False
print True or False
print not True

age = 10
if age >= 18:
    print 'age is', age,'adult'
else:
    print 'age is', age,'teenager'
    
# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
print None
print 0

# 这种变量本身类型不固定的语言称之为动态语言
a = 123 # a是整数
print a
b = a
a = 'ABC' # a变为字符串
print a
print b

# 再议不可变对象
a = ['c', 'b', 'a']
print a
a.sort()
print a

a = 'abc'
b = a.replace('a', 'A')
print 'b is',b
print 'a is',a

# 除法
print 10 / 3
print 10.0/3
print 10%3

print ord('A')
print chr(65)
print u'中文'

#把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法：
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print len(u'ABC')
print len('ABC')
print len(u'中文')

# 在Python中，采用的格式化方式和C语言是一致的，用%实现
print 'Hello, %s' % 'world'
print 'Hi, %s, you have $%04d. 浮点数 %.3f, 十六进制整数 %x' % ('Michael', 100, 12.01, 0xf6)
print 'Age: %s. Gender: %s' % (25, True)
# 用%%来表示一个%
print 'growth rate: %d%%' % 7
