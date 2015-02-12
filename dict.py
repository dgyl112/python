#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年1月8日

@author: lee
使用dict和set

dict全称dictionary，
在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

dict有以下几个特点：
1. 查找和插入的速度极快，不会随着key的增加而增加；
2. 需要占用大量的内存，内存浪费多。
'''

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
d['Adam'] = 67
print d
print d['Adam']

d['Jack'] = 90
d['Jack'] = 88
print d

if 'Thomas' in d:
    print d['Thomas']
else:
    print 'Thomas not in d'
    
print d.get('Thomas')
print d.get('Thomas',-1)

print d
print d.pop('Bob')
print d



'''
Set
set和dict类似，也是一组key的集合，但不存储value。
由于key不能重复，所以，在set中，没有重复的key
'''
s = set([1, 2, 3])
'''注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是
告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。'''
print s
# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print s
s.add(4)
print s
s.add(4)
print s
s.remove(4)
print s


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2



s = set([1, 2, 3])
s.add((1, 2, 3));
print s,'元素个数',len(s)
# error
#s.add((1, [2, 3]))
#print s,'元素个数',len(s)



