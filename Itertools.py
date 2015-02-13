#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
itertools
itertools提供了非常有用的用于操作迭代对象的函数。

itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算。

@author: lee
'''


'''
count()会创建一个无限的迭代器，所以下面代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
'''
import itertools
natuals = itertools.count(1)
for n in natuals:
    print n
    if n > 100:
        break


'''
cycle()会把传入的一个序列无限重复下去
'''
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
time = 0
for c in cs:
    time += 1
    print c
    if time > 10:
        break
   

'''
repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
'''
# 打印5次'N'
ns = itertools.repeat('N', 5)
for n in ns:
    print n

'''
takewhile()等函数根据条件判断来截取出一个有限的序列
'''
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n


'''
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
'''
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
for c in itertools.chain('ABC', 'XYZ'):
    print c

'''
groupby()把迭代器中相邻的重复元素挑出来放在一起
'''
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, group            # A <itertools._grouper object at 0x00000000020B4518>
    print key, list(group)      # A ['A', 'A', 'A']

# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)      # A ['A', 'a', 'a']



'''
imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕
'''
r = itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1))
print r                         # <itertools.imap object at 0x00000000021C46D8>
for x in r:
    print x                     # 10        40        90

r = map(lambda x: x*x, [1, 2, 3])
print r                         # [1, 4, 9] r已经计算出来了 


'''
类似imap()这样能够实现惰性计算的函数就可以处理无限序列：
'''
r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x<100, r):
    print n

'''
map()不能处理无限序列，否则会耗尽内存，死机
'''
# r = map(lambda x: x*x, itertools.count(1))    # 死机

'''
ifilter()就是filter()的惰性实现。
'''