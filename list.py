#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年1月8日

@author: lee
'''
# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0],classmates[1],classmates[len(classmates) - 1]
# 注意数组越界
print classmates[-1],classmates[-2],classmates[-3]

classmates.append('Adam')
print classmates
classmates.insert(1, 'Jack')
print classmates
print "删除list末尾的元素",classmates.pop()
print classmates
print "删除指定位置的元素", classmates.pop(1)
print classmates
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print classmates

L = ['Apple', 123, True]
print L
s = ['python', 'java', ['asp', 'php'], 'scheme']
print s,'元素个数',len(s)

L = []
print L,'元素个数',len(L)


# tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print classmates

t = (1, 2)
print t
t = ()
print t
# 括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
t = (1)
print t
t = (1,)
print t


# “可变的”tuple
# 要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
t = ('a', 'b', ['A', 'B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t


# 条件判断
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 1
if x:
    print 'x:', x,'True'

age = 8
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'
    
# 循环    
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
    
sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum