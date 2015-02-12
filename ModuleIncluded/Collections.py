#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
collections是Python内建的一个集合模块，提供了许多有用的集合类。

@author: lee
'''


'''
namedtuple
namedtuple('名称', [属性list])
'''
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
print Point                 # <class '__main__.Point'>
p = Point(1, 2)
print p.x,p.y
# p.x = 3                   # AttributeError: can't set attribute
print isinstance(p, Point)  # True
print isinstance(p, tuple)  # True

# 用坐标和半径表示一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])

'''
deque
高效实现插入和删除操作的双向列表，适合用于队列和栈
deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
'''
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q                      # deque(['y', 'a', 'b', 'c', 'x'])

'''
defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict

注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
'''
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1'] # abc
print dd['key2'] # N/A


'''
OrderedDict
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
如果要保持Key的顺序，可以用OrderedDict
注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
'''
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# dict的Key是无序的
print d                         # {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict的Key是有序的
print od                        # OrderedDict([('a', 1), ('b', 2), ('c', 3)])


# 按照插入的Key的顺序返回
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print od.keys()                 # ['z', 'y', 'x']


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        # like java: XX ? true: false
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)


fifo = LastUpdatedOrderedDict(3)
fifo[1] = 1             # add: (1, 1)
fifo[2] = 2             # add: (2, 2)
fifo[3] = 3             # add: (3, 3)
fifo[4] = 4             # remove: (1, 1)        add: (4, 4)
fifo[3] = 3             # set: (3, 3)
print fifo              # LastUpdatedOrderedDict([(2, 2), (4, 4), (3, 3)])

'''
Counter
Counter是一个简单的计数器，例如，统计字符出现的个数
Counter实际上也是dict的一个子类
'''
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c                 # Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})

print c['g']            # 2
print c['r']            # 2
print c['i']            # 1
